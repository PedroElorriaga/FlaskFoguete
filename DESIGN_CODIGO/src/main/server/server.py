from flask import Flask
from src.main.routes.calculator_1 import calculators_route_1
from src.main.routes.calculator_2 import calculators_route_2

app = Flask(__name__)
app.register_blueprint(calculators_route_1, url_prefix='/calculator1')
app.register_blueprint(calculators_route_2, url_prefix='/calculator2')
