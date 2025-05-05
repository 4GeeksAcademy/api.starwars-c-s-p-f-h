""" from flask import Blueprint, jsonify, request

from models import db, Planet, People, Favorite, User
planets_bp = Blueprint('planets', __name__, url_prefix='/planets')


@planet_bp.route('/', methods=["GET"])
def get_all_planets():
    list_planets = Planet.get_planets(False)
    return jsonify(list_planets)


@planet_bp.route('/', methods=["POST"])
def create_planet():
    data_request = request.get_json()
    if not 'planet_name' in data_request or not 'film_appearance' in data_request or not 'exploted' in data_request or not 'population' in data_request :
        return jsonify({"error": "Los siguientes campos son obligatorios: name,film_appearance, population "}), 400

    planet_id = data_request["planet_id"]
   planet = Planet.query.get_or_404(planet_id)

    new_planet = Planet(
        planet_name=data_request["name"],
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


@planet_bp.route('/register', methods=["POST"])
def register_planet():
    data_request = request.get_json()
    if not 'student_id' in data_request or not 'planet_id' in data_request:
        return jsonify({"error": "Los siguientes campos son necesario:student_id, planet_id"})

    student = Student.query.get_or_404(data_request["student_id"])
    planet = planet.query.get_or_404(data_request["planet_id"])

    if planet in student.planets:
        return jsonify({"error": "Este curso ya se encuentra registrado"}), 409

    student.planets.append(planet)

    try:
        db.session.commit()
        return jsonify({"message": f"Se registro el curso correctamente para {student.name}"}), 200
    except Exception as e:
        db.session.rollback()
        print("Error", e)
        return jsonify({"error": "Error en el servidor"}) """