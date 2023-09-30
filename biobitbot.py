import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from aiogram import F
from aiogram.filters import Command
import os
import keyboards as kb
from misc import help_message

from handlers import begin, add_biobits, add_sport, add_alcohol, view_biobits, analyze_biobits

load_dotenv()
TelegramToken = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TelegramToken)
dp = Dispatcher()

dp.include_router(begin.router)
dp.include_router(add_biobits.router)
dp.include_router(add_sport.router)
dp.include_router(add_alcohol.router)
dp.include_router(view_biobits.router)
dp.include_router(analyze_biobits.router)

@dp.message(Command("help"))
async def process_help_command(message: types.Message):
    await message.answer(help_message)


@dp.message(Command("clear"))
async def process_help_command(message: types.Message):
    await message.answer(help_message)


@dp.callback_query(F.data == "btn_add_bits")
async def add_bits(callback: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                        reply_markup=kb.inline_kb_beats.as_markup())


@dp.callback_query(F.data == "btn_sports")
async def add_bits(callback: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                        reply_markup=kb.inline_kb_sports.as_markup())


@dp.callback_query(F.data == "btn_drinks")
async def add_bits(callback: types.CallbackQuery, ):
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                        reply_markup=kb.inline_kb_drinks.as_markup())


@dp.callback_query(F.data == "home")
async def add_bits(callback: types.CallbackQuery):
    await bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id,
                                        reply_markup=kb.inline_kb_begin.as_markup())


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
