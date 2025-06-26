import jwt


class JWTHandler:
    def encode_jwt(self, payload: dict) -> str:
        jwt_encoded = jwt.encode(
            payload,
            key='abc123def456',
            algorithm='HS256'
        )

        return jwt_encoded

    def decode_jwt(self, jwt_encoded: jwt) -> dict:
        jwt_decoded = jwt.decode(
            jwt_encoded, key='abc123def456', algorithms='HS256')

        return jwt_decoded
