from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.markdown import text

help_message = text(
    "/start",
    "/help",
    sep="\n"
)


class States(StatesGroup):
    home_state = State()
    weight_state = State()

