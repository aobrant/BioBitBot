from aiogram import Router, F, types
from aiogram.filters import Command

from keyboards import inline_kb_begin

router = Router()


@router.message(Command("start"))
async def process_start_command(message: types.Message):
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )





