import discord
import os
from dotenv import load_dotenv
from src.message_processor import MessageProcessor
from src.watcher import Watcher
import ctypes
import ctypes.util

load_dotenv()
TOKEN = os.environ['PRIVATE_KEY']
DEV_MODE = os.getenv('DEV_MODE', False)
watcher = Watcher()
load_dotenv()
if not DEV_MODE:
    discord.opus.load_opus(ctypes.util.find_library('opus'))


class UltimateBot(discord.Client):
    message_processor = MessageProcessor()

    async def on_ready(self):
        print(f'{client.user} Ultimate discord BOT connected!')
        print(client.guilds)
        print(client.users)

    async def on_message(self, message):
        if message.author == client.user:
            return
        is_response, response_message = await self.message_processor.parse(message, client, discord)
        if is_response:
            message_length = len(response_message)
            if len(response_message) > 2000:
                await message.channel.send(f'Discord dopuszcza wiadomości <=2000 znaków, a to coś ma {message_length}')
            else:
                await message.channel.send(response_message)
        # await watcher.check(message)


client = UltimateBot()
client.run(TOKEN)
