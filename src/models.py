from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    #establish relations
    favorites_list = db.relationship('Favorites', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    img_url = db.Column(db.String(120))
    #establish relations
    favorite = db.relationship('Favorites', backref='characters', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "img_url": self.img_url,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    img_url = db.Column(db.String(120))
    #establish relation
    favorite = db.relationship('Favorites', backref='planets', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "img_url": self.img_url,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_id = db.Column(db.Integer, db.ForeignKey(Characters.id))
    planet_id = db.Column(db.Integer, db.ForeignKey(Planets.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "char_id": self.char_id,
            "planet_id": self.planet_id,
        }