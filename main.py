import os
import discord
import ctypes.util
from dotenv import load_dotenv

from src.client import UltimateBotClient

load_dotenv()
TOKEN = os.getenv('PRIVATE_KEY', '')
DEV_MODE = os.getenv('DEV_MODE', False)

if not DEV_MODE:
    discord.opus.load_opus(ctypes.util.find_library('opus'))

client = UltimateBotClient(intents=discord.Intents.all())
client.run(TOKEN)
