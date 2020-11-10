from models.base_model import db
from models.light import Light
from models.air_conditioner import AirC

def run():
    db.create_all()


if __name__ == "__main__":
    run()
