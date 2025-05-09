from flask import Flask
from src.routes.calculators import calculators_route

app = Flask(__name__)
app.register_blueprint(calculators_route, url_prefix='/calculator')
