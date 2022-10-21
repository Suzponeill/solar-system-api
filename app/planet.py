from flask import Blueprint, jsonify

class Planet:
    def __init__(self,id, name, description, moons = None):
        self.id = id
        self.name = name
        self.description = description
        if moons is None:
            self.moons = []
        else:
            self.moons = moons


home = Planet(4, 'Earth','A pale blue dot.',["earth's moon"])
mars = Planet(3, 'Mars','A smaller red planet')
jupiter = Planet(5, 'Jupiter', 'A gas giant',['Europa','Ganymede', 'Calysto'])


planets_list = [home, mars, jupiter]
planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planet")

@planet_bp.route("", methods = ["GET"])
def get_all_planets():
    planets = []
    for planet in planets_list:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description":planet.description,
            "moons":planet.moons
        }
        planets.append(planet_dict)
    return jsonify(planets)

@planet_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return {"message": "planet_id must be an integer"},400
    
    for planet in planets_list:
        if planet_id == planet.id:
            return {
            "id": planet.id,
            "name": planet.name,
            "description":planet.description,
            "moons":planet.moons
        },200

    return {"message": f"{planet_id} not found in planets list."}, 404