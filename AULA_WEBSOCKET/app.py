from flask import Flask, request, jsonify, send_file, render_template
from database.database import db
from models.payment import Payment
from datetime import timedelta, datetime
from payments_methods.pix import Pix

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECRET_KEY_WEBSOCKET'

db.init_app(app)


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
def view_test(qrcode_id):
    data_from_db = Payment.query.filter_by(id=qrcode_id).first()

    return render_template('payment.html',
                           host='http://localhost:5000',
                           qrcode=data_from_db.qr_code,
                           value=data_from_db.value,
                           payment_id=data_from_db.id)


if __name__ == '__main__':
    app.run(debug=True)
