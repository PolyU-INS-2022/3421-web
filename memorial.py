from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from werkzeug.utils import secure_filename
from db import db, Memorial, Image, User

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_deceasedName(deceasedName, id=False):
    if id:  
        return db.session.execute(db.select(Memorial).filter_by(id=deceasedName)).scalar_one_or_none()
    return db.session.execute(db.select(Memorial).filter_by(username=deceasedName)).scalar_one_or_none()

def create_memorial():
    # Get form data
    try:
        data = request.form
        name = data['name']
        epitaph = data['epitaph']
        birth_date = datetime.strptime(data['dateOfBirth'], '%Y-%m-%d').date()
        death_date = datetime.strptime(data['dateOfDeath'], '%Y-%m-%d').date()
        memorial_description = data['memorialDescription']
        user = current_user
        if "file" not in request.files:
            flash("Memorial created Failed", "Failed")
            return False
        file = request.files['file']
        if file.name != "" and file and allowed_file(file.filename):
            filename = secure_filename(user.username + str(datetime.now().timestamp()).replace("", ".") + file.filename)
            path = f"static/uploads/{filename}"
            file.save(path)
            image = Image(filename=filename, path=path)
            db.session.add(image)
        else:
            flash("Memorial created Failed", "Failed")
            return False
        # Create new memorial
        memorial = Memorial(
            deceasedName=name,
            birth_date=birth_date,
            death_date=death_date,
            epitaph=epitaph,
            memorialDescription=memorial_description,
            user=user.id,
            image=image
        )
        # Save memorial to database
        db.session.add(memorial)
        db.session.commit()

        flash("Memorial created successfully", "success")
        return True
    except Exception:
        flash("Memorial created Failed", "Failed")
        return False

    