import os
import discord
import requests
import json

secret = os.environ['secret'];

client = discord.Client();



@client.event
async def on_ready():
  print('We have logged in')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  



client.run(secret);