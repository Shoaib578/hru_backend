from application import db
from datetime import datetime

class PanelUsers(db.Model):
    panel_userid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),nullable=False,index=True)
    name = db.Column(db.String(200),nullable=False)
    phone = db.Column(db.String(100),nullable=True)
    password = db.Column(db.String(255),nullable=False)
    profile_picture = db.Column(db.String(300),nullable=True)
    title = db.Column(db.String(300),nullable=True)
    description = db.Column(db.Text,nullable=True)
    is_admin = db.Column(db.Integer,nullable=False)
    is_teacher = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime(),nullable=False,default=datetime.utcnow())
    
