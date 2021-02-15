import datetime


class Votekick:
    db = {}
    client = None

    def __init__(self, client):
        self.client = client

    async def run(self, message_object):
        if not message_object.mentions:
            await message_object.channel.send("Podaj kogo mam kiknąć, np, @zajma")

        voted_user = message_object.mentions[0]
        if not (voted_user.id in self.db):
            self.db[voted_user.id] = {
                'counter': 1,
                'last_vote': datetime.datetime.now(),
                'kicks_timestamp': [],
            }
        else:
            if datetime.datetime.now() - self.db[voted_user.id]['last_vote'] > datetime.timedelta(minutes=5):
                self.db[voted_user.id]['counter'] = 0
            self.db[voted_user.id]['last_vote'] = datetime.datetime.now()
            self.db[voted_user.id]['counter'] += 1
            lives = 3 - self.db[voted_user.id]['counter']
            if lives > 0:
                await message_object.channel.send(
                    f'<@!{voted_user.id}> Kolejne ostrzerzenie ziomeczku, jeszcze {lives} i poleci kick! :scream:'
                )

        if self.db[voted_user.id]['counter'] == 3:
            last_24h_kicks = []
            now = datetime.datetime.now()
            for kick_timestamp in self.db[voted_user.id]['kicks_timestamp']:
                if now - kick_timestamp < datetime.timedelta(hours=24):
                    last_24h_kicks.append(kick_timestamp)
            self.db[voted_user.id]['kicks_timestamp'] = last_24h_kicks
            if len(last_24h_kicks) < 2:
                self.db[voted_user.id]['kicks_timestamp'].append(datetime.datetime.now())
                await voted_user.edit(voice_channel=None)
                await message_object.channel.send(f'<@!{voted_user.id}> Leci kick :rage:')
            else:
                await message_object.channel.send('Eghm, za dużo tych kicków, tylko 2 votekicki na 24 godziny')

    def stats(self):
        if not self.db:
            return "nikogo nie trzeba kiknąć"
        return "\n".join([f'<@!{user_id}> voted kick nr: {counter}' for user_id, counter in self.db.items()])
