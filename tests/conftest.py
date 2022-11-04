import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True}) #creates new instance of app

    @request_finished.connect_via(app) #
    def expire_session(sender, response, **extra):
        db.session.remove() #remove the client we create each instance

    with app.app_context(): #create all tables in app
        db.create_all()
        yield app 

    with app.app_context():
        db.drop_all() #drops all databases


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    first_planet = Planet(
        name = "Pluto",
        description= "Not a planet, still our friend.",
        moons = False)
    second_planet = Planet(
        name = "Neptune",
        description= "The sideways one.",
        moons = True)

    db.session.add_all([first_planet, second_planet])
    # Alternatively, we could do
    # db.session.add(first_planet)
    # db.session.add(second_planet)
    db.session.commit()