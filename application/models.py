from application import db

class Artist(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Album(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artist = db.relationship("Artist", backref=db.backref(
        "albums", order_by=id), lazy=True)