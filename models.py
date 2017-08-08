import discord
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

import client
from modules import ModuleLibrary

modules = ModuleLibrary()

# engine = create_engine("sqlite:///ayano.db", echo=True)  # temporarily use sqlite, will set up actual database later
engine = create_engine("sqlite:///:memory:", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)

    def __init__(self):
        raise Exception("User class cannot be instantiated.")


def create_tables():
    Base.metadata.create_all(engine)
