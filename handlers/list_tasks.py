from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.menus import get_quadrants_menu
from services.storage import get_tasks_by_quadrant, mark_task_done

router = Router()

QUADRANT_NAMES = {
    "🔥 Срочно и Важно": 1,
    "📅 Не срочно, но Важно": 2,
    "⚡ Срочно, но не Важно": 3,
    "🗑 Не срочно, не Важно": 4
}

@router.message(F.text == "📋 Мои задачи")
async def show_quadrants(message: Message):
    await message.answer("Выбери квадрант, чтобы посмотреть задачи:", reply_markup=get_quadrants_menu())

@router.message(F.text.in_(QUADRANT_NAMES.keys()))
async def show_tasks_in_quadrant(message: Message):
    quadrant_num = QUADRANT_NAMES[message.text]

    tasks = get_tasks_by_quadrant(message.from_user.id, quadrant_num)

    if not tasks:
        await message.answer("В этом квадранте пока нет невыполненных задач.")
        return

    builder = InlineKeyboardBuilder()
    for task in tasks:
        builder.button(text=f"✅ {task.text}", callback_data=f"done_{task.id}")

    builder.adjust(1)

    await message.answer(
        f"Задачи в квадранте {quadrant_num}:\nНажми на задачу, чтобы отметить её выполненной.",
        reply_markup=builder.as_markup()
    )

@router.callback_query(F.data.startswith("done_"))
async def process_task_done(callback: CallbackQuery):
    task_id_str = callback.data.split("_")[1]
    task_id = int(task_id_str)

    success = mark_task_done(callback.from_user.id, task_id)

    if success:
        await callback.answer("Задача выполнена! Молодец.")
        await callback.message.edit_text(f"✅ Задача выполнена и скрыта из списка.")
    else:
        await callback.answer("Ошибка: задача не найдена.", show_alert=True)