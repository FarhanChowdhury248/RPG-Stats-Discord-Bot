
import discord

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
        
        user_input = message.content
        if user_input.startswith(self.invoker + 'hello'):
            await self.on_hello()
        elif user_input.startswith(self.invoker + 'kill'):
            await self.on_kill()
        
    async def on_hello(self):
        await self.message.channel.send('Hello')

    async def on_kill(self):
        await self.client.logout()