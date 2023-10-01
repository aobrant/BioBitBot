import os

from aiogram import Router, F, types
from aiogram.types import FSInputFile
from aiogram.methods.send_photo import SendPhoto
from aiogram.types import message, callback_query

from keyboards import make_keyboard_from_list, inline_kb_begin
from misc import plot_graph, dec_to_int, counter_for_drinks_per_day, plot_histogram
from sql_integrate import list_items_for_user, list_rec_time

router = Router()

name_list = []


@router.callback_query(F.data == "btn_analyze_bits")
async def analyze_biobits(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    global name_list
    result_list = list_items_for_user(user_id)
    keyboard_markup, name_list = make_keyboard_from_list(result_list)
    await callback.message.answer(
        "Analyze",
        reply_markup=keyboard_markup.as_markup()
    )


@router.callback_query(lambda callback_query: callback_query.data in name_list)
async def on_name_button_click(callback_query: types.CallbackQuery):
    button_text = callback_query.data
    string_to_remove = "new_btn_"
    button_text = button_text.replace(string_to_remove, "")
    user_id = callback_query.from_user.id
    # await callback_query.message.answer(f"{user_id} выбрали имя {button_text}")
    if button_text in ["walk", "run", "cicling", "fitness", "swim", "hike", "tennis", "weight", "sleep_quality"]:
        values, dates, units = list_rec_time(button_text, user_id)
        filepath = plot_graph(user_id, button_text, units, dates, values)
        cat = FSInputFile(filepath)
        await callback_query.message.answer_photo(cat)
        try:
            os.remove(filepath)
        except FileNotFoundError:
            print(f"Файл {filepath} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при удалении файла: {str(e)}")
        await callback_query.message.answer(
            "Hi! I'm BioBitBot 👽 ",
            reply_markup=inline_kb_begin.as_markup())

    if button_text in ["blood_pressure"]:
        values, dates, units = list_rec_time(button_text, user_id)
        pressure_up, pressure_down = dec_to_int(values)
        filepath = plot_graph(user_id, button_text, units, dates, pressure_up, pressure_down)
        cat = FSInputFile(filepath)
        await callback_query.message.answer_photo(cat)
        try:
            os.remove(filepath)
        except FileNotFoundError:
            print(f"Файл {filepath} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при удалении файла: {str(e)}")
        await callback_query.message.answer(
            "Hi! I'm BioBitBot 👽 ",
            reply_markup=inline_kb_begin.as_markup())

    if button_text in ["beer", "wine", "vodka", "whiskey", "rum", "tequila", "gin", "coffee", "water"]:
        values, dates, units = list_rec_time(button_text, user_id)
        days, parameter_counts = counter_for_drinks_per_day(dates, values)
        filepath1 = plot_histogram(user_id, button_text, days, parameter_counts, units)
        cat = FSInputFile(filepath1)
        await callback_query.message.answer_photo(cat)
        try:
            os.remove(filepath1)
        except FileNotFoundError:
            print(f"Файл {filepath1} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при удалении файла: {str(e)}")
        await callback_query.message.answer(
            "Hi! I'm BioBitBot 👽 ",
            reply_markup=inline_kb_begin.as_markup())

