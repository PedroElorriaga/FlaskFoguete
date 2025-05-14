from typing import Dict


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
