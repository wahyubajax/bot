import os
import time
import logging

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineQueryResult
from config import *

StartTime = time.time()

FORMAT = "[Yuu]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
                                                    logging.StreamHandler()], format=FORMAT)
MODULE = []

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


class ConnectionHandler(logging.Handler):
    def emit(self, record):
        for X in ["OSErro", "socket"]:
            if X in record.getMessage():
                os.system(f"kill -9 {os.getpid()} && python3 -m bot")


logger = logging.getLogger()
logger.setLevel(logging.ERROR)

formatter = logging.Formatter("[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M")
stream_handler = logging.StreamHandler()

stream_handler.setFormatter(formatter)
connection_handler = ConnectionHandler()

logger.addHandler(stream_handler)
logger.addHandler(connection_handler)


class Yuu(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, parse_mode=ParseMode.HTML)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, parse_mode=ParseMode.HTML)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()

# User bot
Yuu = Client(
  name="Yuu",
  api_id=API_ID,
  api_hash=API_HASH,
  session_string=SESSION_STRING,
  parse_mode=ParseMode.HTML,
  plugins={"root": "bot/modules"},
)

# Bot nya
Bot = Client(
  name="Bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  in_memory=False,
  parse_mode=ParseMode.HTML,
  plugins={"root": "bot/modules"},
)
