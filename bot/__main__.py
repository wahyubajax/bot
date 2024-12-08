import os
import asyncio
from pyrogram import Client
from importlib import import_module

async def start_clients() -> None:
    log.info("Starting pyrogram client...")

    await asyncio.gather(App.start(), Bot.start())
    log.info("Pyrogram clients started.")


async def stop_clients():
    log.info("Stopping pyrogram client...")

    await asyncio.gather(App.stop(), Bot.stop())
    log.info("Pyrogram clients stopped.")


if __name__ == "__main__":

    loop.logging.disable = True
    loop.run(start_clients(), loop=App.loop, shutdown_callback=stop_clients())
