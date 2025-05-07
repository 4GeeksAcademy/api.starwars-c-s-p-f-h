from flask import Blueprint, jsonify, request
from models import User
from models import db

users_bp=Blueprint('users', __name__,url_prefix="/user")

@users_bp.route('/', methods=['GET'])
def handle_user():
    raw_list_user=User.query.all()
    users_list=[users.serialize() for users in raw_list_user]
    return jsonify(users_list), 200

@users_bp.route('/<int:id>', methods=['GET'])
def handle_single_user(id):
    single_user=User.query.get(id)
    if single_user:
        user_get=single_user.serialize()
        return jsonify(user_get), 200
    else: return jsonify({"Error": "user does not exist"}),404

@users_bp.route('/<int:id>/favorites', methods=['GET'])
def handle_user_favorites(id):
    user=User.query.get(id)
    users_list=user.serialize_with_relations()
    return jsonify(users_list), 200

@users_bp.route('/', methods=['POST'])
def add_new_user():
     request_body = request.get_json()
     
     if not 'name' in request_body or not 'email' in request_body or not 'password' in request_body :
         return jsonify({"error": "Los siguientes campos son obligatorios: name, email, password,"}), 400
     
     new_user=User(
         name=request_body["name"],
         email=request_body["email"],
         password=request_body["password"],
         is_active=request_body["is_active"]
     )
     
     try:
         db.session.add(new_user)
         db.session.commit()
         return ({"Message": "El usuario fue creado con exito"}),200
     except Exception as e:
         db.session.rollback()
         print("Error", e)
         return jsonify({"Error": "Error en el servidor"}),500