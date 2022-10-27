from urllib import response
from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet


# class Planet:
#     def __init__(self,id, name, description, moons = None):
#         self.id = id
#         self.name = name
#         self.description = description
#         if moons is None:
#             self.moons = []
#         else:
#             self.moons = moons


# home = Planet(4, 'Earth','A pale blue dot.',["earth's moon"])
# mars = Planet(3, 'Mars','A smaller red planet')
# jupiter = Planet(5, 'Jupiter', 'A gas giant',['Europa','Ganymede', 'Calysto'])


# planets_list = [home, mars, jupiter]
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

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

# @planet_bp.route("/<planet_id>", methods = ["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         return {"message": "planet_id must be an integer"},400
    
#     for planet in planets_list:
#         if planet_id == planet.id:
#             return {
#             "id": planet.id,
#             "name": planet.name,
#             "description":planet.description,
#             "moons":planet.moons
#         },200

#     return {"message": f"{planet_id} not found in planets list."}, 404