import discord
import os
from dotenv import load_dotenv
from call_to_func import *

load_dotenv()

BOT_INVOKER = '>'

client = discord.Client()

caller = Function_Caller(client, BOT_INVOKER)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):    
    await caller.process_call(message)
    

token = os.getenv('TOKEN')
client.run(token)