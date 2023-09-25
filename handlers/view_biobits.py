from aiogram import Router, F, types
import aiogram.utils.markdown as md

from keyboards import inline_kb_begin
from sql_integrate import count_items_for_user

router = Router()


@router.callback_query(F.data == "btn_view_bits")
async def view_bits(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    results_dict = count_items_for_user(user_id)
    dictionary_content = "\n".join(f"{key}: {value}" for key, value in results_dict.items())
    await callback.message.answer(text=f"Your records:\n{dictionary_content}")
    await callback.message.answer(
        "Hi! I'm BioBitBot 👽 ",
        reply_markup=inline_kb_begin.as_markup()
    )


