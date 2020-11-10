from .base_model import BaseModel, db


class Light(BaseModel, db.Model):
    __tablename__ = 'light'
    name = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, status):
        self.status = status
        self.name = name
        super().__init__()
