
import discord
from RPG_Event import *

EVENTS = []

class Function_Caller:
    def __init__(self, client, invoker):
        self.client = client
        self.invoker = invoker
        self.message = None

    def set_message(self, message):
        self.message = message

    async def process_call(self, message):
        # ignore if bot sent message
        if message.author == self.client.user:
            return
        
        self.set_message(message)
        
        user_input = message.content.split()
        # exit if bot not invoked, otherwise remove invoker
        if user_input[0][0] != self.invoker:
            return
        user_input[0] = user_input[0][1:]
        try:
            if user_input[0] == 'hello':
                await self.on_hello(user_input)
            elif user_input[0] == 'kill':
                await self.on_kill(user_input)
            elif user_input[0] == 'setSession':
                await self.on_set_session(user_input)
        except:
            print('error')
        
    async def on_hello(self, params):
        await self.message.channel.send('Hello')

    async def on_kill(self, params):
        await self.client.logout()

    async def on_set_session(self, params):
        new_event = RPG_Event(params[1], params[2], self.message.author, params[3])
        EVENTS.append(new_event)
        print(EVENTS[-1])
