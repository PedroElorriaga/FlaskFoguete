import bcrypt


class PasswordHandler:
    def hash_password(self, password: str) -> bytes:
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)

        return hash

    def check_password(self, password: str, password_hashed: bytes) -> bool:
        password = password.encode('utf-8')

        if bcrypt.checkpw(password, password_hashed):
            return True
