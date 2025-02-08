import os
import platform
import subprocess
import sys
import traceback
import io
import asyncio
import time
import io
import asyncio
import contextlib
import pyrogram
import html
import time
import uuid

from time import time
from datetime import date
from io import BytesIO, StringIO
from io import BytesIO
import psutil

from meval import meval
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from pyrogram import raw
from bot import Yuu, Bot
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    MessageEntity,
)


from config import *


async def send_large_output(message, output):
    with BytesIO(str.encode(str(output))) as out_file:
        out_file.name = "result.txt"
        await message.reply_document(document=out_file)


async def process_command(message, command):
    result = (await bash(command))[0]
    if int(len(str(result))) > 4096:
        await send_large_output(message, result)
    else:
        await message.reply(f"<pre>{result}</pre>")



@Bot.on_message(filters.command(["e"], prefixes=HANDLER) & filters.user(me))
async def _(client: "bot", message):
    if not get_arg(message):
        return await message.reply("none")
    cmd = message.text.split(maxsplit=3)[1]
    start = datetime.now()
    reply_to_ = message.reply_to_message or message
    file = io.StringIO()
    eval_vars = {
        "c": client,
        "m": message,
        "r": message.reply,
        "bot": Bot,
        "pyrogram": pyrogram,
        "enums": pyrogram.enums,
        "types": pyrogram.types,
        "raw": pyrogram.raw,
        "ikb": InlineKeyboardButton,
    }
    await message.edit("...")
    
    end = datetime.now()
    ping = (end - start).microseconds / 1000

    file = io.StringIO()
    with contextlib.redirect_stdout(file):
        try:
            meval_out = await meval(cmd, globals(), **eval_vars)
            print_out = file.getvalue().strip() or str(meval_out) or "None"
        except Exception as error:
            print_out = str(error)
            
    final_output = f"<pre language=input>{cmd}</pre>\n"
    final_output += f"<pre language=python>{html.escape(print_out)}</pre>"
    final_output += f"<pre language='Time'>{ping}ms</pre>"
    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = str(uuid.uuid4()).split("-")[0].upper() + ".TXT"
    else:
        await reply_to_.reply_text(final_output, quote=True)
    await message.delete()
