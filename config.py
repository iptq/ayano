import os

config = dict()

keys = [
    "client_id",
    "client_secret",
    "token"
]

for key in keys:
    config[key] = os.getenv(key)
