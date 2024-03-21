from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False)
    is_active = db.Column(db.Boolean(), unique=False)
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
    name = db.Column(db.String(120), unique=True)
    height = db.Column(db.String(120))
    weight = db.Column(db.String(120))
    hair_color = db.Column(db.String(120))
    skin_color = db.Column(db.String(120))
    eye_color = db.Column(db.String(120))
    birth_year = db.Column(db.String(120))
    gender = db.Column(db.String(120))
    homeworld = db.Column(db.String(120))
    img_url = db.Column(db.String(240))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "img_url": self.img_url,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    climate = db.Column(db.String(120))
    terrain = db.Column(db.String(120))
    population = db.Column(db.String(120))
    diameter = db.Column(db.String(120))
    gravity = db.Column(db.String(120))
    rotation_period = db.Column(db.String(120))
    orbital_period = db.Column(db.String(120))
    surface_water = db.Column(db.String(120))
    img_url = db.Column(db.String(240))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "surface_water": self.surface_water,
            "img_url": self.img_url,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    char_id = db.Column(db.String(120), nullable=True)
    planet_id = db.Column(db.String(120), nullable=True)
    typeof = db.Column(db.String(120))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "char_id": self.char_id,
            "planet_id": self.planet_id,
            "typeof": self.typeof
        }