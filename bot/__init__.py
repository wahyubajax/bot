import os
import time

from program import Client
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineQueryResult

StartTime = time.time()

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
