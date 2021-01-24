import discord
import os
from src.message_processor import MessageProcessor
from src.watcher import Watcher

TOKEN = os.environ['PRIVATE_KEY']
watcher = Watcher()


class UltimateBot(discord.Client):
    message_processor = MessageProcessor()

    async def on_ready(self):
        print(f'{client.user} Ultimate discord BOT connected!')
        print(client.guilds)
        print(client.users)

    async def on_message(self, message):
        if message.author == client.user:
            return
        is_response, response_message = self.message_processor.parse(message)
        if is_response:
            await message.channel.send(response_message)
        await watcher.check(message)


client = UltimateBot()
client.run(TOKEN)