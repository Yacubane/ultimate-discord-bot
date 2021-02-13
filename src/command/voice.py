import os
from time import sleep
import datetime
from os import listdir
from os.path import isfile, join
import random
from dotenv import load_dotenv
import ctypes
import ctypes.util
import threading

load_dotenv()
DEV_MODE = os.getenv('DEV_MODE', False)


class Voice:
    path = './src/asset/voice'
    path_to_ffmpeg = "./bin/ffmpeg.exe" if DEV_MODE else "./bin/ffmpeg"
    voice_client = None
    voice_channel = None
    last_active_time = None
    is_connected = False
    is_waiting = False

    def __init__(self):
        self.files = [f for f in listdir(self.path) if isfile(join(self.path, f))]

    async def run(self, context, client, discord):
        message = context.content
        title = None
        if len(message) > 8:
            title = message.replace("+płotnik ", '')
        user = context.author
        if user.voice is not None:
            self.voice_channel = user.voice.channel
        if self.voice_channel is None:
            self.voice_channel = self.get_voice_channel(client)
        if self.voice_channel is None:
            await context.channel.send('<@!{user.id}> Nie ma nikogo na głosowym ziomeczku.')
            return

        if not self.is_connected:
            if not DEV_MODE:
                discord.opus.load_opus(ctypes.util.find_library('opus'))
            self.voice_client = await self.voice_channel.connect()
            self.is_connected = True
        self.last_active_time = datetime.datetime.now()
        original_title = title
        title = title + '.mp3' if title is not None else self.rand_item()
        if not isfile(join(self.path, title)):
            await context.channel.send(f'<@!{user.id}> eghm nie ma czegoś takiego jak {original_title}')

        audio_source = discord.FFmpegPCMAudio(
            executable=self.path_to_ffmpeg,
            source=self.path + '/' + title
        )
        if not self.voice_client.is_playing():
            self.voice_client.play(audio_source, after=None)
        self.wait_for_disconnect()

    def get_voice_channel(self, client):
        for server in client.guilds:
            for channel in server.channels:
                if channel.type.name == 'voice':
                    if channel.members:
                        return channel
        return None

    async def check_activity(self):
        await self.voice_client.disconnect()

    def rand_item(self):
        return self.files[random.randint(0, len(self.files) - 1)]

    def wait_for_disconnect(self):
        if not self.is_waiting:
            self.is_waiting = True
            thread = threading.Thread(target=self.thread_fn)
            thread.start()

    def thread_fn(self):
        while self.is_waiting:
            if datetime.datetime.now() - self.last_active_time > datetime.timedelta(minutes=5):
                await self.voice_client.disconnect()
                self.is_waiting = False
            else:
                sleep(60)
