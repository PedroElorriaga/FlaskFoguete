from flask import Blueprint, request, jsonify
from models.meal import Meal
from database.database import db
from datetime import datetime
import pytz

meal_routes = Blueprint('meal', __name__)


@meal_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    nome = data.get('nome')
    descricao = data.get('descricao')
    diet = data.get('diet')

    def make_datetime_action():
        time_br = datetime.now(pytz.timezone('America/Sao_Paulo'))
        time_br_handle = time_br.strftime('%Y-%m-%d %H:%M:%S')

        return time_br_handle

    if nome and descricao and type(diet) == bool:
        new_meal = Meal(nome=nome, descricao=descricao,
                        date=make_datetime_action(), diet=diet,
                        caloria='TESTE')

        db.session.add(new_meal)
        db.session.commit()

        return jsonify({"message": "Item incluido com sucesso!"})

    return jsonify({"message": "Não foi possivel concluir a operação"}), 401


@meal_routes.route('/edit/<meal_id>', methods=['PUT'])
def edit(meal_id):
    data = request.json
    field_to_edit = ['nome', 'descricao', 'diet']

    meal_from_db = Meal.query.filter_by(id=meal_id).first()

    if meal_from_db:
        for field in field_to_edit:
            if field in data:
                setattr(meal_from_db, field, data[field])

        db.session.commit()
        db.session.refresh(meal_from_db)

        return jsonify({"message": "Item alterado com sucesso!"})

    return jsonify({"message": "Item não existe na base de dados"}), 401


@meal_routes.route('/list-all', methods=['GET'])
def list_all():
    meals_from_db = Meal.query.all()

    if meals_from_db:
        meal_list = [{"id": meal.id, "nome": meal.nome,
                      "descricao": meal.descricao,
                      "date": meal.date, "dieta": meal.diet, "caloria": meal.caloria} for meal in meals_from_db]
        return jsonify(meal_list)

    return jsonify({"message": "Não existem nenhum item na base de dados"}), 403


@meal_routes.route('/delete/<meal_id>', methods=['DELETE'])
def delete(meal_id):
    meal_from_db = Meal.query.filter_by(id=meal_id).first()

    if not meal_from_db:
        return jsonify({"message": "O id informado não existe"}), 401

    db.session.delete(meal_from_db)
    db.session.commit()

    return jsonify({"message": "Item deletado com sucesso!"})


@meal_routes.route('/list/<meal_id>', methods=['GET'])
def list(meal_id):
    meal_from_db = Meal.query.filter_by(id=meal_id).first()

    if not meal_from_db:
        return jsonify({"message": "O id informado não existe"}), 401

    return jsonify({"meal": {"id": meal_from_db.id,
                             "nome": meal_from_db.nome,
                             "descricao": meal_from_db.descricao,
                             "date": meal_from_db.date,
                             "dieta": meal_from_db.diet}})
