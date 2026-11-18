from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.menus import get_main_menu
from services.storage import get_user_tasks

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    user_tasks = get_user_tasks(message.from_user.id)

    if not user_tasks:
        welcome_text = (
            "👋 <b>Привет! Я Priority Flow.</b>\n\n"
            "Я помогаю не тонуть в делах и делать вовремя самое важное.\n\n"
            "В основе моей работы — <b>матрица Эйзенхауэра</b>. Когда ты добавляешь задачу, "
            "я спрашиваю: «Она срочная?» и «Она важная?». В зависимости от ответов, "
            "я раскладываю дела по 4 квадрантам:\n\n"
            "🔥 <b>Срочно и Важно</b> — делать прямо сейчас.\n"
            "📅 <b>Не срочно, но Важно</b> — запланировать.\n"
            "⚡ <b>Срочно, но не Важно</b> — делать быстро.\n"
            "🗑 <b>Не срочно, не Важно</b> — отложить.\n\n"
            "Нажми <b>«➕ Добавить задачу»</b>, чтобы создать первую запись."
        )
    else:
        welcome_text = "С возвращением! Рад тебя видеть. Что делаем сегодня?"

    await message.answer(welcome_text, reply_markup=get_main_menu(), parse_mode="HTML")

@router.message(F.text == "🔙 Назад в меню")
async def back_to_menu(message: Message):
    await message.answer(
        "Ты вернулся в главное меню. Выбери действие:",
        reply_markup=get_main_menu()
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = ("🤖 <b>Priority Flow - твой помощник в делах!</b>\n\n"
        "Этот бот помогает расставлять приоритеты по матрице Эйзенхауэра.\n\n"
        "📌 <b>Как пользоваться:</b>\n"
        "1. Нажми кнопку «➕ Добавить задачу».\n"
        "2. Напиши, что нужно сделать.\n"
        "3. Ответь на вопросы о срочности и важности.\n"
        "4. В разделе «📋 Мои задачи» ты можешь увидеть свои дела и отметить их выполненными.\n"
        "5. В разделе «📊 Статистика» следи за своим прогрессом.\n\n"
        "Используй кнопки ниже для управления задачами."
        )
    await message.answer(help_text, reply_markup=get_main_menu(), parse_mode="HTML")