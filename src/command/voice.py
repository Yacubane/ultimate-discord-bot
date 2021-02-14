import os
import random
import discord
import datetime
import threading
import numpy as np
from time import sleep
from os import listdir
from os.path import isfile, join
from src.utils.utils import levenshtein

DEV_MODE = os.getenv('DEV_MODE', False)


class Voice:
    path = './src/asset/voice'
    path_to_ffmpeg = "./bin/ffmpeg.exe" if DEV_MODE else "./bin/ffmpeg"
    voice_client = None
    voice_channel = None
    last_active_time = None
    is_connected = False
    is_waiting = False
    voice_channel_watcher = None
    client = None

    def __init__(self):
        self.files = [f for f in listdir(self.path) if isfile(join(self.path, f))]

    async def run(self, message_object, client):
        message = message_object.content
        self.client = client
        title = None
        if len(message) > 8:
            title = message.replace("+płotnik ", '')
        user = message_object.author
        if user.voice:
            self.voice_channel = user.voice.channel
        if not self.voice_channel:
            self.voice_channel = self.get_voice_channel(client)
        if not self.voice_channel:
            await message_object.channel.send(f'<@!{user.id}> Nie ma nikogo na głosowym ziomeczku.')
            return

        if not self.is_connected:
            await self.connect_to_voice()
        self.last_active_time = datetime.datetime.now()
        original_title = title
        title = self.get_title(title)
        if not title:
            await message_object.channel.send(f'<@!{user.id}> eghm nie ma czegoś takiego jak {original_title}')

        audio_source = discord.FFmpegPCMAudio(
            executable=self.path_to_ffmpeg,
            source=self.path + '/' + title
        )
        if not self.voice_client.is_playing():
            try:
                self.voice_client.play(audio_source, after=None)
            except:
                await self.connect_to_voice()
                self.voice_client.play(audio_source, after=None)
        await self.wait_for_disconnect()

    def get_voice_channel(self, client):
        for server in client.guilds:
            for channel in server.channels:
                if channel.type.name == 'voice':
                    if channel.members:
                        return channel
        return None

    async def connect_to_voice(self):
        self.voice_client = await self.voice_channel.connect()
        self.is_connected = True

    def rand_item(self):
        return self.files[random.randint(0, len(self.files) - 1)]

    async def wait_for_disconnect(self):
        if not self.is_waiting:
            self.is_waiting = True
            threading.Thread(target=self.thread_fn).start()

    def thread_fn(self):
        while self.is_waiting:
            if datetime.datetime.now() - self.last_active_time > datetime.timedelta(minutes=5):
                self.client.loop.create_task(self.voice_client.disconnect())
                self.is_waiting = False
            else:
                sleep(60)

    def get_title(self, title):
        if title:
            if isfile(join(self.path, title + '.mp3')):
                return title + '.mp3'
            else:
                min_distance, result_name = 15, ""
                distance_array = [(levenshtein(title, file_name), file_name) for file_name in self.files]
                for distance_item in distance_array:
                    distance, name = distance_item
                    if min_distance >= distance:
                        min_distance, result_name = distance_item
                if min_distance < 15:
                    return result_name
                else:
                    return None
        else:
            return self.rand_item()
