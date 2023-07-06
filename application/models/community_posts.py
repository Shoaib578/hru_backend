from application import db

class CummunityPosts(db.Model):
    community_post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    description = db.Column(db.String(1000))
    media = db.Column(db.String(300))
    posted_by = db.Column(db.ForeignKey('users.user_id'))
    