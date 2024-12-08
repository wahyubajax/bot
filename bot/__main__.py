import os
import config
import asyncio
from importlib import import_module

from pyrogram import idle
from bot import Yuu , Bot
from pyrogram import Client

async def run_client():
    await Bot.start()
    await Yuu.start()
    await pyrogram.idle()
    await asyncio.gather(*tasks, Yuu.start(), Bot.start())
    await asyncio.gather(loadPlugins(), idle())

print("start")

if __name__ == "__main__":
    Yuu.loop.run_until_complete(run_clients())
