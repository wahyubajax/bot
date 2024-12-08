import os
import config
import asyncio
from bot import Yuu , Bot
from pyrogram import Client

async def main():
    await Bot.start()
    await Yuu.start()
    await pyrogram.idle()
    await asyncio.gather(*tasks, Yuu.start(), Bot.start())

print("start")

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
