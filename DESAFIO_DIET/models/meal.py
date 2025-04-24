from database.database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    diet = db.Column(db.Boolean, nullable=False)
