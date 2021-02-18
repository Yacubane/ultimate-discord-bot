from src.command.trigger import Trigger
from src.watcher_services.hidden_blamer import HiddenBlamer


class Watcher:
    trigger = Trigger()
    hidden_blamer = HiddenBlamer()

    async def check(self, message):
        # await self.trigger.run(message)
        # await self.hidden_blamer.run(message)
