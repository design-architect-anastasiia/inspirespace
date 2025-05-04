from flask import Flask, render_template, request, redirect, url_for
import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
DATA_FILE = 'gallery_data.json'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_gallery():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_gallery(gallery):
    with open(DATA_FILE, 'w') as f:
        json.dump(gallery, f, indent=4)

@app.route('/')
def index():
    gallery = load_gallery()
    return render_template('index.html', gallery=gallery)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            new_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            file.save(file_path)

            title = request.form.get('title', '')
            description = request.form.get('description', '')
            mood = request.form.get('mood', '')
            author = request.form.get('author', 'Anonymous')

            gallery = load_gallery()
            gallery.append({
                'filename': new_filename,
                'title': title,
                'description': description,
                'mood': mood,
                'author': author,
                'timestamp': timestamp
            })
            save_gallery(gallery)

            return redirect(url_for('index'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
