import discord
import os
import random

TOKEN = os.environ['PRIVATE_KEY']


class UltimateBot(discord.Client):
    async def on_ready(self):
        print(f'{client.user} Ultimate discord BOT connected!')
        print(client.guilds)
        print(client.users)

    async def on_message(self, message):
        if message.author == client.user:
            return

        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)


client = UltimateBot()
client.run(TOKEN)
