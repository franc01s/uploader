from werkzeug.utils import secure_filename
import os
from flask import render_template, redirect, url_for, current_app, request, flash, send_from_directory
from . import views


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in current_app.config['ALLOWED_EXTENSIONS']


@views.route('/uploaded')
def uploaded():
    return render_template('views/uploaded.html')



@views.route('/picture/<name>')
def picture(name):
    return render_template('views/picture.html', name=name)


@views.route('/upload', methods=['POST', 'GET'])
# @csrf.exempt
def upload():
    if request.method == 'POST':
        files = request.files
        for f in files:
            myfile = request.files[f]
            if myfile and allowed_file(myfile.filename):
                filename = secure_filename(myfile.filename)
                myfile.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return render_template('views/upload.html')
    else:
        return render_template('views/upload.html')

