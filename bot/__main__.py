import os
import asyncio
from importlib import import_module
from bot import Yuu, Bot


async def main():
    await Yuu.start()
    await Bot.start()
    os.system("rm -rf *session*")
    await asyncio.Event().wait()

print("Botstart")

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())

