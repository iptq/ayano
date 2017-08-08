import discord
import random
import models


def make_client():
    client = discord.Client()

    @client.event
    async def on_ready():
        print("Logged in as {} ({})".format(client.user.name, client.user.id))

    @client.event
    async def on_message(message):
        try:
            print("<{}> {}".format(message.author.id, message.content))
            await models.modules.on_message(client, message)
        except Exception as e1:
            print(e1)

    @client.event
    async def on_message_delete(message):
        content = message.content.replace("@everyone", "@ everyone")
        await client.send_message(message.channel, "<@{}> said: {}".format(message.author.id, content))

    return client
