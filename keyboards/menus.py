from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_main_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="➕ Добавить задачу")
    builder.button(text="📋 Мои задачи")
    builder.button(text="📊 Статистика")

    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True)

def get_quadrants_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="🔥 Срочно и Важно")
    builder.button(text="📅 Не срочно, но Важно")
    builder.button(text="⚡ Срочно, но не Важно")
    builder.button(text="🗑 Не срочно, не Важно")
    builder.button(text="🔙 Назад в меню")

    builder.adjust(2, 2, 1)
    return builder.as_markup(resize_keyboard=True)

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="Да")
    builder.button(text="Нет")

    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
