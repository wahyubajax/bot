import os
import config

async def main():
    await Bot.start()
    await Yuu.start()
    await pyrogram.idle()


if __name__ == "__main__":
    Yuu.loop.run_until_complete(main())
