import discord
import os
from random import randint
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


client.run(os.environ['TOKEN'])