from _decimal import Decimal
import re

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import inline_kb_begin
from misc import States
from sql_integrate import save_data

router = Router()


@router.callback_query(F.data == "btn_beer")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="beer", value_d=1, units_d="cup")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_wine")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="wine", value_d=1, units_d="glass")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_vodka")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="vodka", value_d=1, units_d="shot")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_whiskey")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="whiskey", value_d=1, units_d="shot")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_rum")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="rum", value_d=1, units_d="shot")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_tequila")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="tequila", value_d=1, units_d="shot")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


@router.callback_query(F.data == "btn_gin")
async def slp_ql_1(callback: types.CallbackQuery):
    result = save_data(user_d=callback.from_user.id, parameter_d="gin", value_d=1, units_d="shot")
    if result is not None:
        await callback.message.answer(text="Done .\n")
    else:
        await callback.message.answer(text="Some go wrong\n")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )
