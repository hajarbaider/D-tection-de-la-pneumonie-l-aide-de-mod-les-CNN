from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Image as ReportLabImage


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Clé secrète pour sécuriser les sessions

# 📌 Charger le modèle
model_path = os.path.join(os.getcwd(), "model_coronet_HB (1).h5")
model = tf.keras.models.load_model(model_path)
class_names = ['Normal', 'Bacterial Pneumonia', 'Viral Pneumonia']

# 📌 Configurer l'upload des images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 📌 Fonction pour se connecter à la base de données
def get_db():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

# 📌 Page d'inscription
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if not username or not password:
            flash('Tous les champs sont obligatoires', 'danger')
            return redirect(url_for('register'))
        
        conn = get_db()
        cursor = conn.cursor()
        
        try:
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                           (username, generate_password_hash(password)))
            conn.commit()
            flash('Compte créé avec succès !', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Le nom d’utilisateur existe déjà.', 'danger')
        finally:
            conn.close()
    
    return render_template('register.html')

# 📌 Page de connexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['user'] = username
            flash('Connexion réussie !', 'success')
            return redirect(url_for('home'))
        else:
            flash('Nom d’utilisateur ou mot de passe incorrect', 'danger')
    
    return render_template('login.html')

# 📌 Déconnexion
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Déconnecté avec succès', 'success')
    return redirect(url_for('login'))

# 📌 Page d'accueil (upload & prédiction)
@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith(('png', 'jpg', 'jpeg')):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            img = image.load_img(filepath, target_size=(150, 150))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions)
            result = class_names[predicted_class]
            probability = predictions[0][predicted_class]

            # Stocker les résultats dans la session après conversion
            session['result'] = result
            session['probability'] = float(probability)
            session['filepath'] = filepath

            return render_template('home.html', image=filepath, result=result, probability=probability)

    return render_template('home.html')

@app.route('/')
def index():
    return render_template('index.html')


# 📌 Fonction pour générer le rapport PDF avec l'image et les résultats
def generate_report(result, probability, filepath, logo_path="static/logo.png"):
    if not result or probability is None or not filepath:
        raise ValueError("Les données nécessaires pour générer le rapport sont manquantes.")
    
    report_path = os.path.join("static/uploads", "rapport.pdf")
    
    # Créer le fichier PDF
    c = canvas.Canvas(report_path, pagesize=letter)
    width, height = letter
    
    # 📌 Ajouter une bordure bleue marine
    c.setStrokeColor(colors.darkblue)
    c.setLineWidth(5)
    c.rect(20, 20, width - 40, height - 40)
    
    # 📌 Ajouter le logo en haut du rapport (si disponible)
    logo_path = os.path.join(app.root_path, 'static', 'images', 'log.gif')
    if os.path.exists(logo_path):
        c.drawImage(logo_path, 440, 700, width=150, height=50)

    # 📌 Ajouter le titre du rapport
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(colors.blue)
    c.drawString(100, 700, "Rapport de Prédiction de Pneumonie")
    
    # 📌 Ajouter des informations
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(100, 670, f"Résultat de la prédiction : {result}")
    c.drawString(100, 650, f"Confiance estimée : {probability * 100:.2f}%")
    
    # 📌 Ajouter une ligne horizontale
    c.setStrokeColor(colors.black)
    c.line(100, 630, 500, 630)
    
    # 📌 Ajouter l'image analysée
    c.drawImage(filepath, 200, 400, width=200, height=200)
    
    # Sauvegarder le PDF
    c.showPage()
    c.save()
    
    return report_path


# 📌 Route pour télécharger le rapport
@app.route('/download_report')
def download_report():
    if 'user' not in session:
        flash('Veuillez vous connecter pour accéder à cette fonctionnalité.', 'danger')
        return redirect(url_for('login'))
    
    result = session.get('result')
    probability = session.get('probability')
    filepath = session.get('filepath')
    
    if not result or probability is None or not filepath:
        flash("Les données de la prédiction sont manquantes. Veuillez réessayer.", "danger")
        return redirect(url_for('home'))
    
    report_path = generate_report(result, probability, filepath)
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'rapport.pdf', as_attachment=True)

# 📌 Lancer l'application
if __name__ == '__main__':
    app.run(debug=True)
