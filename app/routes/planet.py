from urllib import response
from flask import Blueprint, jsonify, make_response, request, abort
from app import db
from app.models import planet
from app.models.planet import Planet


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response(jsonify({"message": "planet_id must be an integer"}),400))
    
    matching_planet = Planet.query.get(planet_id)

    if matching_planet is None:
        response_str = f"Planet with id {planet_id} was not found in the database."
        abort(make_response(jsonify({"Message": response_str}), 404))

    return matching_planet

@planet_bp.route("", methods = ["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    moons=request_body['moons'])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.id} successfully created", 201)

@planet_bp.route("", methods = ["GET"])
def get_all_planets():
    response = []
    planets = Planet.query.all()
    for planet in planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description":planet.description,
            "moons":planet.moons
        }
        response.append(planet_dict)
    return jsonify(response)


@planet_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    chosen_planet = validate_planet_id(planet_id)
    return jsonify({
        "id": chosen_planet.id,
        "name": chosen_planet.name,
        "description":chosen_planet.description,
        "moons":chosen_planet.moons
    }),200

@planet_bp.route("/<planet_id>", methods = ["PUT"])
def update_planet(planet_id):
    chosen_planet = validate_planet_id(planet_id)
    request_body = request.get_json()
    
    if "name" not in request_body or "description" not in request_body\
        or "moons" not in request_body:
            return jsonify({"message": "Request must include name, description, and moons."}), 400
    
    chosen_planet.name = request_body["name"]
    chosen_planet.description = request_body["description"]
    chosen_planet.moons = request_body["moons"]
    
    db.session.commit()
    return make_response(f"Planet #{chosen_planet.id} successfully updated",200)

@planet_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_one_planet(planet_id):
    chosen_planet = validate_planet_id(planet_id)
    db.session.delete(chosen_planet)
    db.session.commit()
    return f'Planet #{planet_id} has been deleted',200