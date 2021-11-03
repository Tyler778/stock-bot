import os
import discord
from communicator import get_desc, get_pe

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

  if message.content.startswith("$desc"):
    await message.channel.send(get_desc(message.content.split()[1]))

  if message.content.startswith("$pe"):
    await message.channel.send(get_pe(message.content.split()[1]))

  



client.run(secret);