from flask import Flask
from database.database import db
from routes.meal_routes import meal_routes


app = Flask(__name__)
app.config['SECRET_KEY'] = 'BLABLAcarDUvitao2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@127.0.0.1:3309/desafio-meal'
app.register_blueprint(meal_routes, url_prefix='/meal')

db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
