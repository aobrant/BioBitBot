from _decimal import Decimal

from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.markdown import text
import re

help_message = text(
    "/start",
    "/help",
    sep="\n"
)


class States(StatesGroup):
    home_state = State()
    weight_state = State()
    presure_state = State()
    walk_state = State()
    running_state = State()
    cycling_state = State()
    fitness_state = State()
    swimming_state = State()
    hiking_state = State()
    tennis_state = State()


def text_to_dec(txt):
    pattern = r'(\d{1,3}).*?(\d{1,3})'
    match = re.search(pattern, txt)
    if match:
        err = False
        number1 = int(match.group(1))
        number2 = int(match.group(2))
        number1_str = str(number1)
        number2_str = str(number2)
        combined_str = f"{number1_str}.{number2_str}"
        val = Decimal(combined_str)
    else:
        err = True
    return (val, err)
