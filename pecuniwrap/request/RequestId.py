from uuid import uuid4

class RequestId:
    def __init__(self):
        self.id = uuid4()