from flask import Blueprint, jsonify, request

from models import db, Planet
planets_bp = Blueprint('planets', __name__, url_prefix='/planets')


@planets_bp.route('/', methods=["GET"])
def get_all_planets():
    planets = Planet.query.all()
    list_planets = [planet.serialize() for planet in planets]    
    return jsonify(list_planets)

@planets_bp.route('/<int:id>', methods=["GET"])
def get_one_planet(id):
    one_planet = Planet.query.get(id)
    list_one_planet = one_planet.serialize()
    return jsonify(list_one_planet) 


@planets_bp.route('/', methods=["POST"])
def create_planet():
    data_request = request.get_json()
    if not 'planet_name' in data_request or not 'film_appearance' in data_request or not 'exploted' in data_request or not 'population' in data_request :
        return jsonify({"error": "Los siguientes campos son obligatorios: name,film_appearance, population "}), 400
    
    new_planet = Planet(
        planet_name=data_request["planet_name"],
        film_appearance=data_request["film_appearance"],
        exploted=data_request["exploted"],
        population=data_request["population"]
    )

    try:
        db.session.add(new_planet)
        db.session.commit()
        return jsonify({"message": "Planeta creado con éxito"})
    except Exception as e:
        db.session.rollback()
        print("Error", e)
        return jsonify({"error": "Error en el servidor"})


@planets_bp.route('/<int:id>', methods=["DELETE"])
def delete_planet(id):
    planet = Planet.query.get_or_404(id)
    print(planet)
    try:
        db.session.delete(planet)
        db.session.commit()
        return jsonify({"message": "Planeta borrado con éxito"})
    except Exception as e:
        db.session.rollback()
        print("Error", e)
        return jsonify({"error": "Error en el servidor"})
