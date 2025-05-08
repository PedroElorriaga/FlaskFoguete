# import pytest
from payments_methods.pix import Pix
import os


def test_create_new_pix_request():
    payment_pix_instance = Pix()

    payment_pix = payment_pix_instance.generate_qrcode()

    assert 'bank_payment_id' in payment_pix
    assert 'qr_code' in payment_pix

    qr_code_id = payment_pix['qr_code']

    assert os.path.isfile(f'./static/img/{qr_code_id}.png')

    os.remove(f'./static/img/{qr_code_id}.png')
