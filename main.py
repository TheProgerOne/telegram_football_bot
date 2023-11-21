# main.py
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode, Message
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import datetime

from Data.base import add_user
from func.functions import navigator_buttons
from func.functions import callbeck_bron_data
from func.functions import button_bron_menu

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

token = '5855487509:AAFvQUT4qtmkSCypdLaYKXjjuy2MkO7lNQk'

button_search = KeyboardButton('Поиск свободных полей 🔍')
button_bron = KeyboardButton('Бронировать поля 🔒')

inline_btn_next = InlineKeyboardButton("▶️", callback_data='next_3')
inline_btn_back = InlineKeyboardButton("◀️", callback_data='back_10')
inline_btn_bron = InlineKeyboardButton('Забронировать поля 🔒', callback_data='bron_2')
inline_count = InlineKeyboardButton("1/9", callback_data='1.9')


inline_bron_date = InlineKeyboardButton(f"21-11", callback_data='21-11')
inline_bron_date_back = InlineKeyboardButton('<-', callback_data='date_back')
inline_bron_date_next = InlineKeyboardButton('->', callback_data='date_next')

inline_bron_btn = InlineKeyboardButton("Забронироваить", callback_data='bron')


inline_pay_1h_btn = InlineKeyboardButton('Оплатить 💸', url='https://s.binance.com/lhSHP6w8')
cheek_pay_btn = InlineKeyboardButton('Проверить', callback_data='cheek')


inline_back_menu = InlineKeyboardButton('Назад', callback_data='menu')

button_navigator = InlineKeyboardMarkup()
button_navigator.add(inline_btn_back, inline_btn_next)
button_navigator.row(inline_btn_bron)
button_navigator.row(inline_count)



inline_pay_btn = InlineKeyboardMarkup(row_width=1)
inline_pay_btn.add(inline_pay_1h_btn,cheek_pay_btn,inline_back_menu)



kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kb_menu.add(button_search, button_bron)

bot = Bot(token=token, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot=bot)




@dp.message_handler(commands=['start'])
async def message_handler(message: Message):
    
    add_user(chat_id=message.from_user.id, name=message.from_user.full_name)

    text = "Добро пожаловать в PLSportBot\nЯ помогу тебе в поиске и бронирование футбольных полей."

    await bot.send_message(message.from_user.id, text, reply_markup=kb_menu)


@dp.message_handler()
async def handler_menu(message: Message):
    chat_id = message.from_user.id

    if message.text == "Поиск свободных полей 🔍":
        await bot.copy_message(chat_id=chat_id, from_chat_id=-1001522689909, message_id=2, reply_markup=button_navigator)

@dp.callback_query_handler()
async def agree_ref_start(query: types.callback_query):
    data_str = query.data
    if  data_str.find("next") != -1 or data_str.find("back") != -1:
        message_id = query.data
        message_id = message_id.split('_')[1]
        btn = navigator_buttons(messega_id=message_id)
        
        
        await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
        # await bot.send_message(chat_id=query.message.chat.id, text=message_id)
        await bot.copy_message(chat_id=query.message.chat.id, from_chat_id=-1001522689909, message_id=message_id, reply_markup=btn)


    if  data_str.find("bron") != -1 :
        bron_id = query.data
        bron_id = bron_id.split('_')[1]

        button_brom_menu1 = button_bron_menu(data_str)

        await bot.send_message(chat_id=query.message.chat.id, text=f"Вы хотите забронироваить поля под id:{bron_id}\n\nПожалуйста выберите время:",reply_markup=button_brom_menu1)

    elif data_str == "cheek":
        await bot.send_message(chat_id=query.message.chat.id, text=f"id заявки: #{query.message.chat.id}\n\nВаш заявка отправлена, пожалуйста подождите...")

    elif data_str.find('h') != -1:

        text = callbeck_bron_data(data_str)

        await bot.send_message(chat_id=query.message.chat.id, text=text,reply_markup=inline_pay_btn)

    elif data_str == 'menu':
         await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
         await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id-1)
        
class BookingStates(StatesGroup):
    waiting_for_time = State()

@dp.message_handler(lambda message: message.text == 'Забронировать поле 🔒')
async def handle_booking_request(message: types.Message):
    await message.answer("Пожалуйста, введите время в формате 16:00-20:00")
    await BookingStates.waiting_for_time.set()

@dp.message_handler(lambda message: message.text.count(':') == 1 and '-' in message.text, state=BookingStates.waiting_for_time)
async def handle_time_input(message: types.Message, state: FSMContext):
    entered_time = message.text.strip()
    how_much_time_to_pay = calculate_time_difference(entered_time)

    if how_much_time_to_pay is not None:
        link = generate_payment_link(how_much_time_to_pay)
        await message.answer(f"Спасибо, ваше время бронирования: {entered_time}")
        await message.answer(f"Ссылка для бронирования поля: {link}")
        await state.finish()
    else:
        await message.answer("Неправильный формат времени. Введите время в формате 16:00-20:00")


def calculate_time_difference(input_time):
    # Разделение времени по тире и извлечение начального и конечного времени
    start_time, end_time = input_time.split('-')

    # Разделение часов и минут
    start_hour = int(start_time.split(':')[0])
    end_hour = int(end_time.split(':')[0])

    # Вычисление разницы в часах
    difference = end_hour - start_hour

    return difference


def generate_payment_link(difference):
    if difference == 4:
        return "https://example.com/payment_4_hours"
    elif difference == 3:
        return "https://example.com/payment_3_hours"
    else:
        return "https://example.com/default_payment_link"
    

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True
    )