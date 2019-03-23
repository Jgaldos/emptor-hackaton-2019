from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models


class Verified_ids(BaseModel):
    """model for one of your table"""
    __tablename__ = 'verified_ids'

    id = db.Column(db.Integer, primary_key = True)
    ml_user_id = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def data(self):
        return {'id': self.ml_user_id,
                'score': self.score}



