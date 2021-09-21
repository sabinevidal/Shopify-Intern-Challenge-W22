import os
import sys
import imghdr
from . import db
from flask import Flask, render_template, request, redirect, url_for, abort, flash, jsonify, make_response
from datetime import datetime as dt
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from .models import User, Image
from .forms import UploadImageForm

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/', methods=['GET'])
def home():
    title = "Welcome!"
    description = "Let's begin..."
    return render_template('app/index.html')

@app.route('/upload', methods=['GET'])
def image_create_form():
    form = UploadImageForm()
    return render_template('app/upload.html', form=form)

@app.route('/upload', methods=['POST'])
def image_create():
    form = UploadImageForm()
    description = None
    tags = None
    user_id = None

    if len(request.files.getlist('file')) > 1:
        for file in request.files.getlist('file'):
            image_uploader(file)

        try:
            new_image = Image(description=description, tags=tags, user_id=user_id)
            new_image.insert()
            flash("The image was successfully saved!")

        except Exception as e:
            db.session.rollback()
            print(sys.exc_info())
            flash("A database insertion error occurred. The image wasn't saved.")
            print(e)
        finally:
            db.session.close()

    elif len(request.files.getlist('file')) == 1:
        file = request.files['file']
        image_uploader(file)

        return make_response(f"One Image successfully created!")

    else:
        abort(400)

    # return redirect('/update')
    # return make_response(f"Image successfully created!")

@app.route('/update', methods=['GET'])
def image_update_form():
    form = UploadImageForm()

@app.route('/update', methods=['POST'])
def image_update():
    form = UploadImageForm()
    description = form.description.data
    tags = form.description.data
    user_id = form.user_id.data


@app.route('/register')
def user_create():
    username = request.args.get('user')
    email = request.args.get('email')
    bio = request.args.get('bio')
    if username and email:
        new_user = User(
            username=username,
            email=email,
            bio=bio,
            admin=False
        )
        db.session.add(new_user)
        db.session.commit()
    return make_response(f"{new_user} successfully created!")

def image_uploader(file):
    filename = secure_filename(file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext.lower() not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext.lower() != validate_image(file.stream):
            return "Invalid image", 400
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return file

# -----------------------------------------------------------
# Error Handlers
# -----------------------------------------------------------
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "internal server error"
    }), 422
# @app.errorhandler(AuthError)
# def handle_auth_error(ex):
#     '''
#     Error handling for AuthError
#     '''
#     message = ex.error['description']
#     response = jsonify(ex.error)
#     response.status_code = ex.status_code
#     print('AUTH ERROR: ', response.get_data(as_text=True))
#     flash(f'{message} Please login.')
#     return redirect('/')
