from _decimal import Decimal

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import inline_kb_begin
from misc import States
from sql_integrate import save_data

router = Router()


@router.callback_query(F.data == "weight")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import weight, kg  ",
                                  input_field_placeholder="Выберите способ подачи")
    await state.set_state(States.weight_state)


@router.message(States.weight_state, F.text.regexp(r"^[+]?(?!-)(\d+\.\d+|\d+)$"))
async def i_weight(message: Message, state: FSMContext):
    await state.update_data(weight=Decimal(message.text))
    user_data = await state.get_data()
    await message.answer(text=f"Weight {user_data['weight']} .\n")
    save_data(user_d=message.from_user.id, parameter_d="weight", value_d=user_data['weight'], units_d="kg")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
    await state.clear()


@router.message(States.weight_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect weight"
    )
