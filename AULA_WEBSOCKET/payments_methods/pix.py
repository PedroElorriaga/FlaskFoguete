import qrcode
import uuid


class Pix:
    def __init__(self):
        pass

    def generate_qrcode(self):
        bank_payment_id_simulation = str(uuid.uuid4())

        # COPY AND PAST CODE
        hash_payment = f'copy_and_past_{bank_payment_id_simulation}'
        qrcode_img = qrcode.make(hash_payment)
        qrcode_img.save(
            f'static/img/qrcode_payment_{bank_payment_id_simulation}.png')

        return {
            "bank_payment_id": bank_payment_id_simulation,
            "qr_code": f"qrcode_payment_{bank_payment_id_simulation}"
        }
