from flask import Flask, render_template, request, jsonify, redirect, url_for, session, send_file, flash
from flask_cors import CORS
import os
from dotenv import load_dotenv
import openai
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import json
import time
from datetime import datetime
import requests
import io


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    image_data = db.Column(db.Text, nullable=False)  # Base64 encoded image
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/auth')
def auth():
    return redirect(url_for('login'))  # Redirects to login page

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            flash("Username already exists", "error")
            return redirect(url_for('signup'))
        
        if User.query.filter_by(email=email).first():
            flash("Email already exists", "error")
            return redirect(url_for('signup'))
        
        new_user = User(
            username=username, 
            email=email, 
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        
        session['user_id'] = new_user.id
        session['username'] = new_user.username
        return redirect(url_for('dashboard'))
    
    return render_template('auth.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('dashboard'))
        
        flash("Invalid email or password", "error")
        return redirect(url_for('login'))
    
    return render_template('auth.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # List of inspirational quotes about creativity and art
    quotes = [
        "Every artist was first an amateur. — Ralph Waldo Emerson",
        "Creativity takes courage. — Henri Matisse",
        "Art enables us to find ourselves and lose ourselves at the same time. — Thomas Merton",
        "The purpose of art is washing the dust of daily life off our souls. — Pablo Picasso",
        "Art is not what you see, but what you make others see. — Edgar Degas",
        "Imagination is more important than knowledge. — Albert Einstein",
        "Every child is an artist. The problem is how to remain an artist once we grow up. — Pablo Picasso",
        "You don't take a photograph, you make it. — Ansel Adams",
        "The artist's world is limitless. It can be found anywhere, far from where he lives or a few feet away. — Paul Strand",
        "Art is the lie that enables us to realize the truth. — Pablo Picasso"
    ]
    
    # Select a random quote
    import random
    quote = random.choice(quotes)
    
    return render_template('dashboard.html', username=session['username'], quote=quote)

@app.route('/generate')
def generate():
    if 'user_id' not in session:
        return redirect(url_for('auth'))
    
    return render_template('generate.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = User.query.get(session['user_id'])
    images = Image.query.filter_by(user_id=session['user_id']).order_by(Image.created_at.desc()).all()
    
    return render_template('profile.html', user=user, images=images)

@app.route('/api/generate_image', methods=['POST'])
def generate_image():
    if 'user_id' not in session:
        return jsonify({'error': 'Not authenticated'}), 401

    prompt = request.json.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        openai.api_key = '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'

        response = openai.Image.create(
            prompt=prompt,
            model = "dall-e-3",
            n=1,
            size="1024x1024"
        )
        print("OpenAI Response",response)

        image_url = response['data'][0]['url']
        
        image_response = requests.get(image_url)
        image_bytes = image_response.content
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')

        new_image = Image(
            user_id=session['user_id'],
            prompt=prompt,
            image_data=image_base64
        )
        db.session.add(new_image)
        db.session.commit()

        print("INFO: Image saved to database successfully")

        return jsonify({
            'success': True,
            'data': {
                'url': f"data:image/jpeg;base64,{image_base64}",
                'id': new_image.id
            }
        })
    except openai.error.OpenAIError as e:
        return jsonify({'error': str(e)}), 500


@app.route('/download_image/<int:image_id>')
def download_image(image_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    image = Image.query.get_or_404(image_id)
    
    # Check if the image belongs to the logged-in user
    if image.user_id != session['user_id']:
        return "Unauthorized", 403
    
    # Convert base64 to binary
    image_data = base64.b64decode(image.image_data)
    
    # Create a file-like object
    image_bytes = io.BytesIO(image_data)
    
    return send_file(
        image_bytes,
        mimetype='image/jpeg',
        as_attachment=True,
        download_name=f"ai-art-{image_id}.jpg"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

