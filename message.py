from flask import request, flash
from flask_login import current_user
from datetime import datetime
from db import db, Message,Memorial

def create_message():
    user = current_user
    message = Message(
        name = user.username,
        content = request.form["content"],
        created_at = datetime.utcnow(),
        creator = user.id
    )
    # Save message to database
    db.session.add(message)
    db.session.commit()
    flash("Message created successfully", "success")




def get_messages():
    return db.session.execute(db.select(Message)).scalars()