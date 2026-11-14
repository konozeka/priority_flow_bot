from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.menus import get_main_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот Priority Flow. Помогу расставить приоритеты. \n\n"
                         "Нажми на кнопку ниже, чтобы начать.",
                         reply_markup=get_main_menu()
                         )

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