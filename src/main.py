import discord
import os
from dotenv import load_dotenv

load_dotenv()

BOT_INVOKER = '>'

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    # ignore if bot sent message
    if message.author == client.user:
        return
    
    content = message.content
    if content.startswith(BOT_INVOKER + 'hello'):
        await message.channel.send('Hello')
    if content.startswith(BOT_INVOKER + 'kill'):
        await client.logout()

token = os.getenv('TOKEN')
client.run(token)