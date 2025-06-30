import jwt

from settings.env_configs import EnvConfig


class JWTHandler:
    def encode_jwt(self, payload: dict) -> str:
        jwt_encoded = jwt.encode(
            payload,
            key=EnvConfig().JWT_KEY,
            algorithm=EnvConfig().JWT_ALGORITHM
        )

        return jwt_encoded

    def decode_jwt(self, jwt_encoded: str) -> dict:
        jwt_decoded = jwt.decode(
            jwt_encoded, key=EnvConfig().JWT_KEY, algorithms=EnvConfig().JWT_ALGORITHM)

        return jwt_decoded
