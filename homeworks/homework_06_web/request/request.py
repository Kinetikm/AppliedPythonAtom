import uuid

from homeworks.homework_06_web.request.request_type import RequestType


class Request:
    request_type: RequestType

    def __init__(self, request_type, authors=None, title=None, key_words=None, abstract=None):
        self.request_type = request_type
        self.authors = authors
        self.title = title
        self.key_words = key_words
        self.abstract = abstract
        self.request_id = str(uuid.uuid4())
