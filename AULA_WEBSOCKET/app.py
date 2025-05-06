from flask import Flask, request, jsonify, send_file, render_template
from database.database import db
from models.payment import Payment
from datetime import timedelta, datetime
from payments_methods.pix import Pix
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)
socketio = SocketIO(app)


@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.json

    if not data['value']:
        return jsonify({"message": "Informações invalídas"}), 401

    qrcode_instance = Pix()
    qrcode = qrcode_instance.generate_qrcode()

    new_payment_request = Payment(value=data['value'],
                                  expiration_date=datetime.now() + timedelta(minutes=30))

    new_payment_request.bank_payment_id = qrcode['bank_payment_id']
    new_payment_request.qr_code = qrcode['qr_code']

    db.session.add(new_payment_request)
    db.session.commit()

    return jsonify({
        "message": "Solicitação criada com sucesso",
        "payment_info": new_payment_request.to_dict()
    })


@app.route('/payments/pix/qrcode/<file>', methods=['GET'])
def get_qrcode_file(file):
    return send_file(f'static/img/{file}.png', mimetype='image/png')


@app.route('/payments/pix/<qrcode_id>', methods=['GET'])
def view_payment(qrcode_id):
    data_from_db = Payment.query.filter_by(id=qrcode_id).first()

    if data_from_db:
        if data_from_db.paid:
            return render_template('confirmed_payment.html',
                                   host='http://localhost:5000',
                                   qrcode=data_from_db.qr_code,
                                   value=data_from_db.value,
                                   payment_id=data_from_db.id)

        return render_template('payment.html',
                               host='http://localhost:5000',
                               qrcode=data_from_db.qr_code,
                               value=data_from_db.value,
                               payment_id=data_from_db.id)

    return render_template('404.html')


@app.route('/payments/pix/confirmed', methods=['POST'])
def pix_confirmation():
    data = request.json

    payment_from_db = Payment.query.filter_by(
        bank_payment_id=data['bank_payment_id']).first()

    if not payment_from_db:
        return jsonify({"message": "Something wrong with your request"}), 403

    if not data['value'] or data['value'] != payment_from_db.value or payment_from_db.paid:
        return jsonify({"message": "Something wrong with your request"}), 403

    payment_from_db.paid = True

    db.session.commit()
    db.session.refresh(payment_from_db)

    socketio.emit(f'payment-confirmed-{payment_from_db.id}')

    return jsonify({"message": "Payment recived with success"})


@socketio.on('connect')
def client_connection():
    print('Cliente conectado')


@socketio.on('disconnect')
def client_disconnect():
    print('Cliente desconectado')


if __name__ == '__main__':
    socketio.run(app, debug=True)
