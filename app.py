import os
from flask import Flask, flash, request, redirect, render_template, send_from_directory, url_for
from werkzeug.utils import secure_filename
import test_function as tf

ALLOWED_EXTENSIONS = {'xlsx'}

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'files'

# check input file's file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# home page
@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        # if the user does not select a file, browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # if the user submits a file with the correct format
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file'))
    # render the home page
    return render_template('index.html')

# download page
@app.route('/download', methods=['POST', 'GET'])
def download_file():
    # run the test function
    a, b, c = tf.test()
    # create the result file for downloading
    if request.method == 'POST':
        if request.form['Download Result File'] == 'Download Result File':
            return send_from_directory(app.config['UPLOAD_FOLDER'], 'c.xlsx')
    # render the download page
    return render_template('download.html', a=a, b=b, c=c)

# main
if __name__ == "__main__":
    app.run()