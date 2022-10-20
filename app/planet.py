from flask import Blueprint, jsonify

class Planet:
    def __init__(self,id = None, name = None,description = None, moons = None):
        self.id = id
        self.name = name
        self.description = description
        if self.moons is None:
            self.moons = []
        else:
            self.moons = moons


home = Planet('Earth','A pale blue dot.',["earth's moon"])
mars = Planet('Mars','A smaller red planet')
jupiter = Planet('Jupiter', 'A gas giant',['Europa','Ganymede', 'Calysto'])

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