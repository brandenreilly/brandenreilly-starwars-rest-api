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
    user = User.query.filter_by(username=recieved["username"]).first()
    userdet = user.serialize()
    return jsonify(userdet)

@app.route('/user', methods=['POST'])
def handle_create_user():
    sent_user = request.json
    new_user = User(username=sent_user["username"], password=sent_user["password"], email=sent_user["email"])
    db.session.add(new_user)
    db.session.commit()
    created_user = User.query.filter_by(username=sent_user["username"]).first()
    created_details = created_user.serialize()
    return jsonify(created_details), 200


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
    favs = Favorites.query.filter_by(user_id=sent_fav["user_id"], name=sent_fav["name"]).first()
    if favs:
        return jsonify("Favorite Exists"), "403 Favorite already exists."
    else:
        new_fav = Favorites(**sent_fav)
        db.session.add(new_fav)
        db.session.commit()
        recent_added = Favorites.query.filter_by(user_id=sent_fav["user_id"], name=sent_fav["name"])
        if recent_added:
            new_favs = Favorites.query.all()
            listed = list(map(lambda x: x.serialize(), new_favs))
            return(jsonify(listed)), 200
        else:
            return jsonify("Record not added."), "409 Record has not been added."
    
@app.route('/favorites/<uid>/<id>', methods=['DELETE'])
def handle_delete_favorite(uid,id):
    to_delete = Favorites.query.get(id)
    db.session.delete(to_delete)
    db.session.commit()
    new_favs = Favorites.query.filter_by(user_id=uid)
    listed = list(map(lambda x: x.serialize(), new_favs))
    return jsonify(listed), 200

@app.route('/favorites/all/<uid>', methods=['DELETE'])
def handle_delete_all_favorites(uid):
    find_favs = Favorites.query.filter_by(user_id=uid)
    list_favs = list(map(lambda x: x.serialize(), find_favs))
    db.session.delete(list_favs)
    db.session.commit()
    return jsonify("ALL FAVORITES FROM USER HAS BEEN DELETED"), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
