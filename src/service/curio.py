import os
import threading
import time
import requests
from pymongo import MongoClient

IG_USER_ID = os.getenv('IG_USER_ID', '')
IG_SESSION_ID = os.getenv('IG_SESSION_ID', '')
MDB_HOST = os.getenv('MDB_HOST', '')
MDB_USER = os.getenv('MDB_USER', '')
MDB_PASSWORD = os.getenv('MDB_PASSWORD', '')
MDB_NAME = os.getenv('MDB_NAME', '')


class Curio:
    interval = 3600
    insta_url = 'https://www.instagram.com/graphql/query/' \
                '?query_hash=003056d32c2554def87228bc3fd9668a' \
                '&variables={%22id%22:%228688821894%22,%22first%22:1}'
    mongoClient = MongoClient(
        f'mongodb+srv://{MDB_USER}:{MDB_PASSWORD}@{MDB_HOST}/{MDB_NAME}?retryWrites=true&w=majority'
    )

    def __init__(self, client):
        self.thread = None
        self.client = client
        self.db = self.mongoClient.zarzecze_db.config_collection
        # self.db.delete_many({})

        self.curio_channel = self.get_text_channel_by_name('ciekawostawka')
        if not self.curio_channel:
            self.curio_channel = self.get_text_channel_by_name('general')
        if not self.curio_channel:
            print("nie ma kanału na ciekawostki :/")
            return

        self.thread = threading.Thread(target=self.job)
        self.thread.start()

    def get_text_channel_by_name(self, name):
        for server in self.client.guilds:
            for channel in server.channels:
                if channel.type.name == 'text' and channel.name == name:
                    return channel
        return None

    def get_last_url(self):
        item = self.db.find_one()
        if item:
            return item['_id'], item['last_instagram_image']
        return None, None

    def set_last_url(self, url):
        self.db.update({'type': 'instagram'}, {'type': 'instagram', 'last_instagram_image': url}, True)

    def job(self):
        while True:
            self.client.loop.create_task(self.async_job())
            time.sleep(self.interval)

    async def async_job(self):
        cookies = {
            'ds_user_id': IG_USER_ID,
            'sessionid': IG_SESSION_ID
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.150 Safari/537.36',
        }
        self.interval = 3600
        data = requests.get(self.insta_url, headers=headers, cookies=cookies)
        try:
            data = data.json()
        except:
            print("Nie udało się pobrać zdjęcia z instagrama")
            await self.curio_channel.send("KRZYCHU! we tam napraw bo token z IG wygasł :/")
            self.interval = 3600 * 12
            return
        items = data['data']['user']['edge_owner_to_timeline_media']['edges']
        is_list = False
        if isinstance(items, list):
            image_url = items[0]['node']['display_url']
            image_id = items[0]['node']['id']
            is_list = True
        else:
            image_url = items['node']['display_url']
            image_id = items['node']['id']
        _, db_img_id = self.get_last_url()
        if image_id == db_img_id:
            return
        if is_list:
            for item in items:
                await self.curio_channel.send(item['node']['display_url'])
        else:
            await self.curio_channel.send(image_url)
        self.set_last_url(image_id)
