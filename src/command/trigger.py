import csv


class Trigger:
    triggers = {}

    def __init__(self):
        with open('./src/asset/trigger.csv', encoding="utf8") as csvfile:
            data = csv.DictReader(csvfile)
            for item in data:
                if not (item['name'] in self.triggers):
                    self.triggers[item['name']] = []
                self.triggers[item['name']].append(item['trigger'].lower())

    async def run(self, args):
        message = args.content.lower()
        message = message[:500]
        for user, triggers in self.triggers.items():
            for trigger in triggers:
                if trigger in message:
                    await args.channel.send(f'HALO, {user}! ktoś użył trigger word "{trigger}"')
                    return
