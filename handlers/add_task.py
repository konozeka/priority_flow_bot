from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.task_states import AddTaskStates
from keyboards.menus import get_yes_no_kb, get_main_menu
from services.storage import add_task

router = Router()

@router.message(F.text == "➕ Добавить задачу")
async def start_add_task(message: Message, state: FSMContext):
    await state.set_state(AddTaskStates.waiting_for_text)
    await message.answer("Напиши текст задачи (что нужно сделать?):")

@router.message(AddTaskStates.waiting_for_text)
async def process_task_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await state.set_state(AddTaskStates.waiting_for_urgent)
    await message.answer("Это срочно?", reply_markup=get_yes_no_kb())

@router.message(AddTaskStates.waiting_for_urgent, F.text.in_({"Да", "Нет"}))
async def process_urgent(message: Message, state: FSMContext):
    is_urgent = (message.text == "Да")
    await state.update_data(urgent=is_urgent)
    await state.set_state(AddTaskStates.waiting_for_important)
    await message.answer("Это важно?", reply_markup=get_yes_no_kb())

@router.message(AddTaskStates.waiting_for_important, F.text.in_({"Да", "Нет"}))
async def process_important(message: Message, state: FSMContext):
    is_important = (message.text == "Да")

    user_data = await state.get_data()

    new_task = add_task(
        user_id=message.from_user.id,
        text=user_data['text'],
        urgent=user_data['urgent'],
        important=is_important
    )

    await state.clear()

    await message.answer(
        f"Задача сохранена! Она попала в квадрант {new_task.quadrant()}.",
        reply_markup=get_main_menu()
    )