from flask import request as flaskRequest


class MockRequestCalculator2:
    def __init__(self, body: flaskRequest) -> None:  # type: ignore
        self.json = body
