# functions.py
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def navigator_buttons(messega_id):
    bron_id = messega_id
    messega_id = int(messega_id) + 1
    messega_id_back = messega_id -2

    if messega_id == 11:
        messega_id = 2

    if messega_id == 3:
        messega_id_back = 10

    inline_btn_next = InlineKeyboardButton("▶️", callback_data=f"next_{messega_id}")
    inline_btn_back = InlineKeyboardButton("◀️", callback_data=f"back_{messega_id_back}")
    inline_btn_bron = InlineKeyboardButton('Забронировать поля 🔒', callback_data=f"bron_{bron_id}")

    button_navigator = InlineKeyboardMarkup()
    button_navigator.add(inline_btn_back, inline_btn_next)
    button_navigator.row(inline_btn_bron)

    return button_navigator
