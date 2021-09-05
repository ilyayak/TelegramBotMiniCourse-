import asyncio

from aiogram import Bot, Dispatcher, executor
from config import TOKEN


loop = asyncio.get_event_loop()
bot = Bot(TOKEN,parse_mod ="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__=="__main__":
