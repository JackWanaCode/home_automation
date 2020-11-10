from .base_model import BaseModel, db


class AirC(BaseModel, db.Model):
    __tablename__ = 'air_con'
    power = db.Column(db.Boolean, nullable=False)
    temp = db.Column(db.Integer, nullable=False)

    def __init__(self, power, temp):
        self.power = power
        self.temp = temp
        super().__init__()
