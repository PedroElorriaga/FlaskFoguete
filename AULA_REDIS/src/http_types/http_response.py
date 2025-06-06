class HttpResponse:
    def __init__(self, body: dict = None, status: int = None) -> None:
        self.body = body
        self.status = status
