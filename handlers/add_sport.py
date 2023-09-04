from _decimal import Decimal
import re

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import inline_kb_begin
from misc import States
from sql_integrate import save_data

router = Router()


@router.callback_query(F.data == "btn_walk")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import distance, km  ")
    await state.set_state(States.walk_state)


@router.message(States.walk_state, F.text.regexp(r"^[+]?(?!-)(\d+\.\d+|\d+)$"))
async def i_weight(message: Message, state: FSMContext):
    await state.update_data(walk=Decimal(message.text))
    user_data = await state.get_data()
    result = save_data(user_d=message.from_user.id, parameter_d="walk", value_d=user_data['walk'], units_d="km")
    if result is not None:
        await message.answer(text="Done .\n")
    else:
        await message.answer(text="Some go wrong\n")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
    await state.clear()


@router.message(States.walk_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect distance"
    )


@router.callback_query(F.data == "btn_run")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import distance, km  ")
    await state.set_state(States.running_state)


@router.message(States.running_state, F.text.regexp(r"^[+]?(?!-)(\d+\.\d+|\d+)$"))
async def i_weight(message: Message, state: FSMContext):
    await state.update_data(run=Decimal(message.text))
    user_data = await state.get_data()
    result = save_data(user_d=message.from_user.id, parameter_d="run", value_d=user_data['run'], units_d="km")
    if result is not None:
        await message.answer(text="Done .\n")
    else:
        await message.answer(text="Some go wrong\n")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
    await state.clear()


@router.message(States.running_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect distance"
    )


@router.callback_query(F.data == "btn_cycling")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import distance, km  ")
    await state.set_state(States.cycling_state)


@router.message(States.cycling_state, F.text.regexp(r"^[+]?(?!-)(\d+\.\d+|\d+)$"))
async def i_weight(message: Message, state: FSMContext):
    await state.update_data(cicling=Decimal(message.text))
    user_data = await state.get_data()
    result = save_data(user_d=message.from_user.id, parameter_d="cicling", value_d=user_data['cicling'], units_d="km")
    if result is not None:
        await message.answer(text="Done .\n")
    else:
        await message.answer(text="Some go wrong\n")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
    await state.clear()


@router.message(States.cycling_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect distance"
    )


@router.callback_query(F.data == "btn_gym")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import time, hr")
    await state.set_state(States.fitness_state)


@router.message(States.fitness_state, F.text.regexp(r"^[+]?(?!-)(\d+\.\d+|\d+)$"))
async def i_weight(message: Message, state: FSMContext):
    await state.update_data(fitness=Decimal(message.text))
    user_data = await state.get_data()
    result = save_data(user_d=message.from_user.id, parameter_d="fitness", value_d=user_data['fitness'], units_d="hr")
    if result is not None:
        await message.answer(text="Done .\n")
    else:
        await message.answer(text="Some go wrong\n")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
    await state.clear()


@router.message(States.fitness_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect time"
    )


@router.callback_query(F.data == "btn_swim")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import time, hr")
    await state.set_state(States.swimming_state)


@router.message(States.swimming_state, F.text.regexp(r"^[+]?(?!-)(\d+\.\d+|\d+)$"))
async def i_weight(message: Message, state: FSMContext):
    await state.update_data(swim=Decimal(message.text))
    user_data = await state.get_data()
    result = save_data(user_d=message.from_user.id, parameter_d="swim", value_d=user_data['swim'], units_d="hr")
    if result is not None:
        await message.answer(text="Done .\n")
    else:
        await message.answer(text="Some go wrong\n")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
    await state.clear()


@router.message(States.swimming_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect time"
    )


@router.callback_query(F.data == "btn_hike")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import time, hr")
    await state.set_state(States.hiking_state)


@router.message(States.hiking_state, F.text.regexp(r"^[+]?(?!-)(\d+\.\d+|\d+)$"))
async def i_weight(message: Message, state: FSMContext):
    await state.update_data(hike=Decimal(message.text))
    user_data = await state.get_data()
    result = save_data(user_d=message.from_user.id, parameter_d="hike", value_d=user_data['hike'], units_d="hr")
    if result is not None:
        await message.answer(text="Done .\n")
    else:
        await message.answer(text="Some go wrong\n")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
    await state.clear()


@router.message(States.hiking_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect time"
    )


@router.callback_query(F.data == "btn_tennis")
async def add_bits(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Import time, hr")
    await state.set_state(States.tennis_state)


@router.message(States.tennis_state, F.text.regexp(r"^[+]?(?!-)(\d+\.\d+|\d+)$"))
async def i_weight(message: Message, state: FSMContext):
    await state.update_data(tennis=Decimal(message.text))
    user_data = await state.get_data()
    result = save_data(user_d=message.from_user.id, parameter_d="tennis", value_d=user_data['tennis'], units_d="hr")
    if result is not None:
        await message.answer(text="Done .\n")
    else:
        await message.answer(text="Some go wrong\n")
    await message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
    await state.clear()


@router.message(States.tennis_state)
async def weight_incorrect(message: Message):
    await message.answer(
        text="Incorrect time"
    )
