import requests

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '12371263817623812638716238716'

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    pass

# create job
@dp.message_handler(commands=['create_job'])
async def create_job():
    pass

# delete job
@dp.message_handler(commands=['delete_job'])
async def delete_job():
    pass

# send to all users
async def send_to_all():
    pass

    
if __name__ == '__main__':
    executor.start_polling(dp)