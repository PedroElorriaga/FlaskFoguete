from flask import request as flaskRequest


class MockRequest:
    def __init__(self, body: flaskRequest) -> None:  # type: ignore
        self.json = body
