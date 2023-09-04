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
    presure_state = State()
    walk_state = State()
    running_state = State()
    cycling_state = State()
    fitness_state = State()
    swimming_state = State()
    hiking_state = State()
    tennis_state = State()

