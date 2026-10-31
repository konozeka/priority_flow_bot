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