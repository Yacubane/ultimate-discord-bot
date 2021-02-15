import discord
from src.utils.utils import rand_item


class HiddenBlamer:

    responses = [
        lambda author: f"Niewidoczni, tacy jak <@!{author.id}> nie mają prawa głosu!",
        lambda author: f"<@!{author.id}>, proszę zmienić status na online",
        lambda author: "Niewidoczni nie mają prawa głosu!",
        lambda author: "Niewidoczni nie mają racji!",
        lambda author: "Jak jesteś niewidoczny to nawet nie załanczaj komputera",
        lambda author: "Niewidoczni są ignorowani",
        lambda author: "Niewidoczni to oszukiści",
        lambda author: "Okej, spoko, ale niewidoczni nie mają prawa głosu",
        lambda author: "Kto to powiedział?",
        lambda author: "Ej nie słyszymy!",
        lambda author: "Oj, ktoś coś mówił?",
        lambda author: "Chyba się przesłyszałem",
        lambda author: "Ktoś coś mówił?",
        lambda author: "Halo, ktoś coś mówił?",
        lambda author: "Kto nie słyszy?",
        lambda author: "Halo?!",
        lambda author: "Czy ktoś z państwa słyszał coś?",
        lambda author: "Ludzie, przecież tu nikogo nie ma"
    ]

    async def run(self, args):
        author = args.author
        if author.status == discord.Status.offline:
            await args.channel.send(rand_item(self.responses)(author))
