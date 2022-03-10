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
  
    if message.content.startswith('!Бен хелп'):
      await message.channel.send('Что бы начать работу напиши !Бен .........')

  
    if message.content.startswith('!Бен'):
      yes_number = 1
      no_number = 2
      hm_number = 3
      haha_number = 4
      current_number = randint(1, 4)
      if current_number == yes_number:
        await message.channel.send('Да')
      if current_number == no_number:
        await message.channel.send('Нет')
      if current_number == hm_number:
        await message.channel.send('Хм')      
      if current_number == haha_number:
        await message.channel.send('Хахаха')

client.run(os.environ['TOKEN'])