class Planet:
    def __init__(self,id = None, name = None,description = None, moons = None):
        self.id - id
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