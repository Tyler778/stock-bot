import os
import discord
from communicator import get_basic

secret = os.environ['secret'];

client = discord.Client();



@client.event
async def on_ready():
  print('We have logged in')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$test"):
    await message.channel.send("Test success")

  if message.content.startswith("$basic"):
    await message.channel.send(get_basic(message.content.split()[1]))

  



client.run(secret);