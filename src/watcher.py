from src.command.trigger import Trigger


class Watcher:
    trigger = Trigger()

    async def check(self, message):
        await self.trigger.run(message)
