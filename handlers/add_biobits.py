from _decimal import Decimal
import re

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import inline_kb_begin
from misc import States, text_to_dec
from sql_integrate import save_data

router = Router()


@router.callback_query(F.data == "weight")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import weight, kg  ")
    await state.set_state(States.weight_state)


@router.message(States.weight_state, F.text.regexp(r'^[+-]?(\d{0,3}[,.]?\d{0,3}|\d{0,3})$'))
async def i_weight(message: Message, state: FSMContext):
    text = message.text
    val, err = text_to_dec(text)
    if not err:
        await state.update_data(weight=Decimal(val))
    else:
        await message.answer(text="Some go wrong\n")
    user_data = await state.get_data()
    result = save_data(user_d=message.from_user.id, parameter_d="weight", value_d=val, units_d="kg")
    if result is not None:
        await message.answer(text="Done .\n")
    else:
        await message.answer(text="Some go wrong\n")
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


@router.callback_query(F.data == "btn_s1")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="sleep_quality", value_d=1, units_d="-")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_s2")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="sleep_quality", value_d=2, units_d="-")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_s3")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="sleep_quality", value_d=3, units_d="-")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_s4")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="sleep_quality", value_d=4, units_d="-")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_s5")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="sleep_quality", value_d=5, units_d="-")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_coffee")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="coffee", value_d=1, units_d="cup")
    print(result)
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_water")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="water", value_d=1, units_d="liter")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_pressure")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import blood pressure in format up/down")
    await state.set_state(States.presure_state)


@router.message(States.presure_state, F.text.regexp(
    r"^(([1-3]\d{0,2})|([4-9]\d{0,1}))[^\d](([1-3]\d{0,2})|([4-9]\d{0,1}))$"))
async def i_weight(message: Message, state: FSMContext):
    text = message.text
    pattern = r'(\d{1,3}).*?(\d{1,3})'
    match = re.search(pattern, text)
    if match:
        number1 = int(match.group(1))
        number2 = int(match.group(2))
        number1_str = str(number1)
        number2_str = str(number2)
        if number1 > number2:
            combined_str = f"{number1_str}.{number2_str}"
        else:
            combined_str = f"{number2_str}.{number1_str}"
        pressure = Decimal(combined_str)
        # await state.update_data(pressure=Decimal(combined_str))
        # user_data = await state.get_data()
        result = save_data(user_d=message.from_user.id, parameter_d="blood_pressure", value_d=pressure, units_d="mP")
        if result is not None:
            await message.answer(text="Done .\n")
        else:
            await message.answer(text="Some go wrong\n")
    else:
        await message.answer(text="Some go wrong\n")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup())
    await state.clear()


@router.message(States.presure_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect pressure"
    )
