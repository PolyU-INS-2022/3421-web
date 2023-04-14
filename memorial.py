import os

from flask import request, flash
from flask_login import current_user
from datetime import datetime
from werkzeug.utils import secure_filename
from db import db, Memorial, Image

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_deceasedName(deceasedName, id=False):
    if id:  
        return db.session.execute(db.select(Memorial).filter_by(id=deceasedName)).scalar_one_or_none()
    return db.session.execute(db.select(Memorial).filter_by(username=deceasedName)).scalar_one_or_none()

def create_memorial():
    # Get form data
    if not os.path.exists("static/uploads/"):
        os.mkdir("static/uploads/")
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
        filename = secure_filename(user.username + str(datetime.now().timestamp()).replace(".", "") + file.filename)
        print(filename)
        path = f"static/uploads/{filename}"
        file.save(path)
        image = Image(filename=filename, path=path)
        db.session.add(image)
        db.session.commit()
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
        image=image.id
    )
    # Save memorial to database
    db.session.add(memorial)
    db.session.commit()
    flash("Memorial created successfully", "success")
    return True


def get_memorials():
    return db.session.execute(db.select(Memorial)).scalars()

def get_latest_deceased():
    return db.session.query(Memorial).order_by(Memorial.death_date.desc()).limit(3).all()

def get_images():
    return db.session.execute(db.select(Image)).scalars()

def get_latest_memorials_with_images():
    # Fetch the latest 3 memorials
    latest_memorials = db.session.query(Memorial).order_by(Memorial.death_date.desc()).limit(3).all()
    
    # For each memorial, fetch the associated image
    memorials_with_images = []
    for memorial in latest_memorials:
        image = db.session.query(Image).join(Memorial).filter(Memorial.id == memorial.id).first()
        memorials_with_images.append((memorial, image))
        
    return memorials_with_images

def get_memorials_by_user(user_id):
    return db.session.query(Memorial).filter_by(user=user_id).all()


def get_images_by_user(user_id):
    return db.session.query(Image).join(Memorial).filter(Memorial.user == user_id).all()







