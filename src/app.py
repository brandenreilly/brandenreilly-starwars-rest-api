"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_user_hello():

    all_users = User.query.all()
    response_body = list(map(lambda x: x.serialize(), all_users))

    return jsonify(response_body), 200

@app.route('/getuser', methods=['POST'])
def handle_get_user():
    recieved = request.json
    user = User.query.filter_by(username=recieved["username"])
    listed = list((map(lambda x: x.serialize(), user)))
    return jsonify(listed)

@app.route('/user', methods=['POST'])
def handle_user_login():
    sent_user = request.json
    new_user = User(**sent_user)
    db.session.add(new_user)
    db.session.commit()
    all_users = User.query.all()
    new_list = list(map(lambda x: x.serialize(), all_users))
    return(jsonify(new_list))


@app.route('/characters', methods=['GET'])
def handle_characters_hello():

    all_characters = Characters.query.all()
    response_body = list(map(lambda x: x.serialize(), all_characters))

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def handle_planets_hello():

    all_planets = Planets.query.all()
    response_body = list(map(lambda x: x.serialize(), all_planets))

    return jsonify(response_body), 200

@app.route('/favorites', methods=['GET'])
def handle_favorites_hello():

    all_favorites = Favorites.query.all()
    response_body = list(map(lambda x: x.serialize(), all_favorites))

    return jsonify(response_body), 200

@app.route('/favorites/<int:uid>', methods=['GET'])
def handle_user_fav(uid):
    user_fav = Favorites.query.filter_by(user_id=uid)
    listed = list(map(lambda x: x.serialize(), user_fav))
    return jsonify(listed), 200



@app.route('/favorites', methods=['POST'])
def handle_create_favorite():
    sent_fav = request.json
    new_fav = Favorites(**sent_fav)
    db.session.add(new_fav)
    db.session.commit()
    new_favs = Favorites.query.all()
    listed = list(map(lambda x: x.serialize(), new_favs))
    return(jsonify(listed))


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
