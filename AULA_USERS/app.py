from flask import Flask, request, jsonify
from database import db
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from Models.user import User

import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'BLABLAcarDUvitao2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@127.0.0.1:3308/flask-foguete'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    """"
        - Identifique o usuário logado em cada requisição.
        - Carregue o objeto do usuário para que ele possa ser usado em outras 
        partes do código, como em verificações de permissões ou exibição de 
        informações personalizadas.
    """
    return User.query.get(int(user_id))


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout bem-sucedido"})


@app.route('/login', methods=['POST'])
def login():
    try:
        if current_user.id:
            return jsonify({"message": "Faça o logout da conta atual"}), 401
    except:
        pass

    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # Verifica se o usuário existe
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            # Aqui você pode adicionar a lógica para criar um token ou iniciar uma sessão
            return jsonify({"message": "Login bem-sucedido"})

    return jsonify({"message": "Credenciais inválidas"}), 401


@app.route('/all-users', methods=['GET'])
@login_required
def all_users():
    users = User.query.all()
    user_list = [{"id": user.id, "username": user.username} for user in users]
    return jsonify(user_list)


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(str.encode(password), salt)

    if username and password:
        user_exists = User.query.filter_by(username=username).first()

        if not user_exists:
            new_user = User(username=username,
                            password=password_hashed, role='user')

            # ADDING IN DB
            db.session.add(new_user)
            db.session.commit()

            return jsonify({"message": f"{username} foi criado com sucesso!"})

        return jsonify({"message": "Usuário ja existe"}), 401


@app.route('/update', methods=['PUT'])
@login_required
def update():
    data = request.json
    user_from_db = User.query.filter_by(id=current_user.id).first()

    for field in ['username', 'password']:
        if field in data:
            if field == 'password':
                salt = bcrypt.gensalt()
                password_hashed = bcrypt.hashpw(str.encode(data[field]), salt)
                setattr(user_from_db, field, password_hashed)
                continue
            else:
                # getattr(obj, nome_do_atributo)
                if data[field] != getattr(user_from_db, field):
                    # setattr(obj, nome_do_atributo, valor)
                    setattr(user_from_db, field, data[field])
                else:
                    return jsonify({"message": "Nenhuma alteração foi feita"})

    db.session.commit()
    db.session.refresh(user_from_db)

    return jsonify({"message": "Usuario atualizado com sucesso"})


@app.route('/update-admin/<user_id>', methods=['PUT'])
@login_required
def update_admin(user_id):
    data = request.json
    user_from_db = User.query.filter_by(id=user_id).first()

    if current_user.role != 'admin':
        return jsonify({"message": "Operação não permitida"}), 403

    for field in ['username', 'password']:
        if field in data:
            if field == 'password':
                salt = bcrypt.gensalt()
                password_hashed = bcrypt.hashpw(str.encode(data[field]), salt)
                setattr(user_from_db, field, password_hashed)
                continue
            else:
                # getattr(obj, nome_do_atributo)
                if data[field] != getattr(user_from_db, field):
                    # setattr(obj, nome_do_atributo, valor)
                    setattr(user_from_db, field, data[field])
                else:
                    return jsonify({"message": "Nenhuma alteração foi feita"})

    db.session.commit()
    db.session.refresh(user_from_db)

    return jsonify({"message": "Usuario atualizado com sucesso"})


@app.route('/delete/<user_id>', methods=['DELETE'])
@login_required
def delete(user_id):
    user_from_db = User.query.filter_by(id=user_id).first()

    def make_delete_action(user):
        db.session.delete(user)
        db.session.commit()

    if user_from_db:
        if current_user.role == 'user' and current_user.id == user_from_db.id:
            logout_user()
            make_delete_action(user_from_db)
            return jsonify({"message": "Usuario deletado com sucesso"})

        elif current_user.role == 'admin':
            make_delete_action(user_from_db)
            return jsonify({"message": "Usuario deletado com sucesso"})

        else:
            return jsonify({"message": "Operação não permitida"}), 403

    return jsonify({"message": "Usuario não existe"}), 401


@app.route('/home', methods=['GET'])
def home():
    return 'Home'


if __name__ == '__main__':
    app.run(debug=True)
