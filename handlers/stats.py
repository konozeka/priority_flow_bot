from aiogram import Router, F
from aiogram.types import Message

from services.storage import get_stats

router = Router()

@router.message(F.text == "📊 Статистика")
async def show_statistics(message: Message):
    stats = get_stats(message.from_user.id)
    total = stats["total"]
    completed = stats["completed"]

    if total == 0:
        await message.answer("У тебя пока нет задач. Самое время добавить первую!")
        return

    percent = int((completed / total) * 100)

    text = (
        f"📊 <b>Твоя статистика:</b>\n\n"
        f"Всего добавлено задач: {total}\n"
        f"Выполнено: {completed} ({percent}%)\n\n"
    )

    if percent == 100:
        text += "Ого, ты выполнил(а) всё! Так держать! 🔥"
    elif percent > 50:
        text += "Отличный темп, больше половины уже сделано! 👍"
    else:
        text += "Главное — не останавливаться. Всё получится! 🚀"

    await message.answer(text, parse_mode="HTML")
