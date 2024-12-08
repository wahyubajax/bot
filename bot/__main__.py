import os
import asyncio
from pyrogram import Client
from importlib import import_module
from pyrogram import Yuu, Bot
async def main():
    await Bot.start()
    await Yuu.starr()
    os.system("rm -rf *session*")
    await asyncio.Event().wait()


print("Berhasil menjalankan semua module!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())
