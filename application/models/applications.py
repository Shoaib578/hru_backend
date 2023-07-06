from application import db

class Applications(db.Model):
    application_id = db.Column(db.Integer,primary_key=True)
    resume = db.Column(db.String(200))
    email = db.Column(db.String(200))
    