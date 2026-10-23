from aiogram.fsm.state import State, StatesGroup

class AddTaskStates(StatesGroup):
    waiting_for_text = State()
    waiting_for_urgent = State()
    waiting_for_important = State()