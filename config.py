import os

keys = [
    "client_id",
    "client_secret",
    "token"
]


class Config():
    def __init__(self):
        for key in keys:
            setattr(self, key, os.getenv(key.upper()))


def make_config():
    return Config()
