import discord
from src.message_processor import MessageProcessor
from src.watcher import Watcher


class UltimateBotClient(discord.Client):
    # watcher = Watcher()
    message_processor = MessageProcessor()

    async def on_ready(self):
        print(f'{self.user} Ultimate discord BOT connected!')
        print(self.guilds)
        print(self.users)

    async def on_message(self, message):
        if message.author == self.user:
            return
        is_response, response_message = await self.message_processor.parse(message, self)
        if is_response:
            message_length = len(response_message)
            if len(response_message) > 2000:
                await message.channel.send(f'Discord dopuszcza wiadomości <=2000 znaków, a to coś ma {message_length}')
            else:
                await message.channel.send(response_message)
        # await watcher.check(message)