import discord
from src.message_processor import MessageProcessor
from src.watcher import Watcher
from src.service.curio import Curio


class UltimateBotClient(discord.Client):
    # watcher: Watcher = Watcher()
    message_processor: MessageProcessor = None
    services = []

    async def on_ready(self):
        print(f'{self.user} Ultimate discord BOT connected!')
        self.services.append(Curio(self))
        self.message_processor = MessageProcessor(self)

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
