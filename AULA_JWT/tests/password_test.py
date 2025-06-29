from src.security.password_handler import PasswordHandler


def test_password_hash_handler():
    password_handler = PasswordHandler()
    hashed_password = password_handler.hash_password('testingPass123')
    checked_password_match = password_handler.check_password(
        'testingPass123', hashed_password)

    assert checked_password_match
    assert isinstance(hashed_password, bytes)
