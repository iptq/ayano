import asyncio
import random

import discord

from config import config
from models import engine
from modules import ModuleLibrary

client = discord.Client()
modules = ModuleLibrary()


@client.event
async def on_ready():
    print("Logged in as {} ({})".format(client.user.name, client.user.id))


messages = [
    "im not a bot",
    "what do u want NigA",
    "kys",
    "stop hling me u bich",
    "owo",
    "im gya",
    "d",
    "can just shut up",
    "idb lo"
]


@client.event
async def on_message(message):
    print(message.author.id, message.content)
    if message.content.startswith("<@{}>".format(client.user.id)):
        await client.send_message(message.channel, random.choice(messages))


@client.event
async def on_message_delete(message):
    content = message.content.replace("@everyone", "@ everyone")
    await client.send_message(message.channel, "<@{}> said: {}".format(message.author.id, content))

if __name__ == "__main__":
    print("Starting...")
    client.run(config.token)
