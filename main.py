from flask import Flask, flash, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from functions.face_utils import allowed_file, processImage

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.secret_key = 'secret'

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        operation = request.form.get("operation")
        if 'file' not in request.files:
            flash("No image is selected", "danger")
            return "No file part", 400
        file = request.files['file']
        print("received image", file.filename)
        if file.filename == "":
            flash("No image is selected", "danger")
            return request.url, 400
        if file and allowed_file(file.filename):
            # Ensure the uploads directory exists
            upload_folder = app.config['UPLOAD_FOLDER']
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
                print(f"Created upload directory: {upload_folder}")

            filename = secure_filename(file.filename)
            file_path = os.path.join(upload_folder, filename)
            print(f"Saving file to: {file_path}")
            file.save(file_path)
            new_filename = processImage(filename, operation)
            if new_filename:
                flash(f"Your image has been processed and is available <a href='/uploads/{new_filename.split('/')[-1]}' target='_blank'>here</a>", "success")
            else:
                flash("An error occurred while processing your image.", "danger")
            return render_template("home.html")
    return render_template('home.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if "__main__" == __name__:
    app.run(debug=True, port=5001)
