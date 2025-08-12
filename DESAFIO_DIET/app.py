from flask import Flask
from flask_migrate import Migrate
from database.database import db
from routes.meal_routes import meal_routes
from configs.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(meal_routes, url_prefix='/meal')

db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)
