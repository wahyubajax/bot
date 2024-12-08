import os
import time
import logging

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineQueryResult
from config import API_ID, API_HASH, BOT_TOKEN, SESSION

StartTime = time.time()

FORMAT = "[Yuu]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
                                                    logging.StreamHandler()], format=FORMAT)
MODULE = []

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
  session_string=SESSION,
  parse_mode=ParseMode.HTML,
  plugins=dict(root="bot"),
)

# Bot nya
Bot = Client(
  name="Bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN,
  in_memory=False,
  parse_mode=ParseMode.HTML,
  plugins=dict(root="bot"),
)
