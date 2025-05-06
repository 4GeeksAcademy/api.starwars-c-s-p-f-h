from flask import Blueprint, jsonify, request
from models import Favorite, User, Planet, People
from models import db

favorites_bp=Blueprint('favorites', __name__,url_prefix="/favorites")

@favorites_bp.route('/', methods=['GET'])
def handle_Favorite():
    raw_list_favorite=Favorite.query.all()
    users_list=[favorites.serialize() for favorites in raw_list_favorite]
    return jsonify(users_list), 200


@favorites_bp.route('/planet', methods=['POST'])
def add_new_favorite_planet():
     request_body = request.get_json()
     
     if not 'user_id' in request_body or not 'planet_id' in request_body :
         return jsonify({"error": "Los siguientes campos son obligatorios: user_id, planet_id"}), 400
     
     user_id=request_body["user_id"]
     planet_id=request_body["planet_id"]
     user=User.query.get_or_404(user_id)
     planet=Planet.query.get_or_404(planet_id)
     raw_list_favorite=Favorite.query.filter_by(planet_id=planet_id)
     user_list=[favorites.serialize() for favorites in raw_list_favorite]
     if len(user_list)!=0:
      if user_list[0]["planet_id"]==planet_id and user_list[0]["user_id"]==user_id:
        return jsonify({"Error":"ya tienes este planeta en favoritos"}),400

     new_favorite=Favorite(
         user_id=request_body["user_id"],
         planet_id=request_body["planet_id"],
         person_id=request_body["person_id"]
       
     )
     
     try:
         db.session.add(new_favorite)
         db.session.commit()
         return ({"Message": "El Planeta fue Añadido con exito"}),200
     except Exception as e:
         db.session.rollback()
         print("Error", e)
         return jsonify({"Error": "Error en el servidor"}),500
     
@favorites_bp.route('/planet/<int:id>', methods=['DELETE'])
def delete_favorite_planet(id):
     request_body = request.get_json()
     user_id=request_body["user_id"]
     planet=Planet.query.get_or_404(id)
     raw_list_favorite=Favorite.query.filter_by(person_id=id, user_id=user_id).first()
     
    
     try:
        db.session.delete(raw_list_favorite)
        db.session.commit()
        return ({"Message": "El Planeta fue Eliminado con exito"}),200
     except Exception as e:
         db.session.rollback()
         print("Error", e)
         return jsonify({"Error": "Error en el servidor"}),500
     
@favorites_bp.route('/people', methods=['POST'])
def add_new_favorite_people():
     request_body = request.get_json()
     
     if not 'user_id' in request_body or not 'person_id' in request_body :
         return jsonify({"error": "Los siguientes campos son obligatorios: user_id, people_id"}), 400
     
     user_id=request_body["user_id"]
     people_id=request_body["person_id"]
     user=User.query.get_or_404(user_id)
     people=People.query.get_or_404(people_id)
     raw_list_favorite=Favorite.query.filter_by(person_id=people_id)
     user_list=[favorites.serialize() for favorites in raw_list_favorite]
     if len(user_list)!=0:
      if user_list[0]["person_id"]==people_id and user_list[0]["user_id"]==user_id:
        return jsonify({"Error":"ya tienes este personaje en favoritos"})
    
     
     new_favorite=Favorite(
         user_id=request_body["user_id"],
         planet_id=request_body["planet_id"],
         person_id=request_body["person_id"]
       
     )
     
     try:
         db.session.add(new_favorite)
         db.session.commit()
         return ({"Message": "El Personaje fue Añadido con exito"}),200
     except Exception as e:
         db.session.rollback()
         print("Error", e)
         return jsonify({"Error": "Error en el servidor"}),500
     

@favorites_bp.route('/people/<int:id>', methods=['DELETE'])
def delete_favorite_people(id):
     request_body = request.get_json()
     user_id=request_body["user_id"]
     people=People.query.get_or_404(id)
     raw_list_favorite=Favorite.query.filter_by(person_id=id, user_id=user_id).first()
     print(raw_list_favorite)
    
     try:
        db.session.delete(raw_list_favorite)
        db.session.commit()
        return ({"Message": "El Personaje fue Eliminado con exito"}),200
     except Exception as e:
         db.session.rollback()
         print("Error", e)
         return jsonify({"Error": "Error en el servidor"}),500
     

