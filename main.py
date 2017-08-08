import asyncio

from client import make_client
from config import make_config
from models import create_tables, engine

if __name__ == "__main__":
    print("Starting...")
    create_tables()
    client = make_client()
    config = make_config()
    client.run(config.token)
