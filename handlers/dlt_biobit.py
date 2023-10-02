from aiogram import Router, F, types

from keyboards import make_keyboard_from_list, make_keyboard_del_from_list, inline_kb_begin
from misc import States
from sql_integrate import list_items_for_user, base_remove
from aiogram.fsm.context import FSMContext

router = Router()


@router.callback_query(F.data == "btn_dlt")
async def dlt_biobits(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.dlt_state)
    user_id = callback.from_user.id
    global name_list
    result_list = list_items_for_user(user_id)
    keyboard_markup, name_list = make_keyboard_del_from_list(result_list)
    await callback.message.answer(
        "Delete 🙀 ",
        reply_markup=keyboard_markup.as_markup()
    )


@router.callback_query(States.dlt_state, lambda callback_query: callback_query.data in name_list)
async def on_name_button_click_del(callback_query: types.CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    button_text = callback_query.data
    string_to_remove = "new_btn_"
    button_text = button_text.replace(string_to_remove, "")
    base_remove(button_text, user_id)
    await state.clear()
    await callback_query.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup())

