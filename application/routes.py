# app/routes.py
import os
from flask import render_template, request, redirect, url_for
from app import app

# specify the upload folder for the images
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('for_page.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    # save the file to the specified upload folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('view', filename=filename))

@app.route('/view/<filename>')
def view(filename):
    # display the uploaded image on a separate page
    return render_template('view.html', filename=filename)
