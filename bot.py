import asyncio
import logging
from aiogram import Bot, Dispatcher, types

TOKEN =8084921352:AAE7iK_Wwk_O836lAG0I6c_eH_bptO2_QAQ

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет! Я твой бот.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())