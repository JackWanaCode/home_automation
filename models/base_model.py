from datetime import datetime
from api import app
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
db = SQLAlchemy(app)


class BaseModel():
    id = db.Column(db.String, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self):
        self.id = str(uuid4())
        self.date_created = datetime.utcnow()

    def add(self):
        print(self)
        self.date_updated = datetime.utcnow()
        db.session.add(self)
        db.session.commit()

    def save(self):
        self.date_updated = datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)
