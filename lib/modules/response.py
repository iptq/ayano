import random

responses = [
    "im not a bot",
    # "what do u want NigA",
    # "kys",
    # "stop hling me u bich",
    # "owo",
    # "im gya",
    # "d",
    # "can just shut up",
    # "idb lo"
]


async def on_mention(client, message):
    await client.send_message(message.channel, random.choice(responses))


async def addresponse(client, message, args):
    if len(args) == 2:
        responses.append(args[1])

commands = dict(
    addresponse=addresponse
)
