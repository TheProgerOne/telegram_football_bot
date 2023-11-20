# main.py
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode, Message
from aiogram.utils import executor

from Data.base import add_user
from func.functions import navigator_buttons

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

token = '5855487509:AAFvQUT4qtmkSCypdLaYKXjjuy2MkO7lNQk'

button_search = KeyboardButton('Поиск свободных полей 🔍')
button_bron = KeyboardButton('Бронировать поля 🔒')

inline_btn_next = InlineKeyboardButton("▶️", callback_data='next_3')
inline_btn_back = InlineKeyboardButton("◀️", callback_data='back_10')
inline_btn_bron = InlineKeyboardButton('Забронировать поля 🔒', callback_data='bron_2')

inline_bron_btn_09_10 = InlineKeyboardButton("09-10 🔒", callback_data='09-10_h')
inline_bron_btn_10_11 = InlineKeyboardButton("10-11 🔒", callback_data='10-11_h')
inline_bron_btn_11_12 = InlineKeyboardButton("11-12 🔒", callback_data='11-12_h')
inline_bron_btn_12_13 = InlineKeyboardButton("12-13 🔒", callback_data='12-13_h')
inline_bron_btn_13_14 = InlineKeyboardButton("13-14", callback_data='13-14_h')
inline_bron_btn_14_15 = InlineKeyboardButton("14-15", callback_data='14-15_h')
inline_bron_btn_15_16 = InlineKeyboardButton("15-16", callback_data='15-16_h')
inline_bron_btn_16_17 = InlineKeyboardButton("16-17 🔒", callback_data='16-17_h')
inline_bron_btn_17_18 = InlineKeyboardButton("16-17 🔒", callback_data='17-18_h')
inline_bron_btn_18_19 = InlineKeyboardButton("18-19", callback_data='18-19_h')
inline_bron_btn_19_20 = InlineKeyboardButton("19-20", callback_data='19-20_h')
inline_bron_btn_20_21 = InlineKeyboardButton("20-21", callback_data='20-21_h')
inline_bron_btn_21_22 = InlineKeyboardButton("21-22", callback_data='21-22_h')
inline_bron_btn_22_23 = InlineKeyboardButton("22-23", callback_data='22-23_h')
inline_bron_btn_23_00 = InlineKeyboardButton("22-23", callback_data='23-00_h')

inline_pay_1h_btn = InlineKeyboardButton('Оплатить 💸', url='https://s.binance.com/lhSHP6w8')


inline_back_menu = InlineKeyboardButton('Назад', callback_data='menu')

button_navigator = InlineKeyboardMarkup()
button_navigator.add(inline_btn_back, inline_btn_next)
button_navigator.row(inline_btn_bron)

button_brom_menu = InlineKeyboardMarkup(row_width=3)
button_brom_menu.add(inline_bron_btn_09_10,inline_bron_btn_10_11,inline_bron_btn_11_12,
                     inline_bron_btn_12_13,inline_bron_btn_13_14,inline_bron_btn_14_15,
                     inline_bron_btn_15_16,inline_bron_btn_16_17,inline_bron_btn_17_18,
                     inline_bron_btn_18_19,inline_bron_btn_19_20,inline_bron_btn_20_21,
                     inline_bron_btn_21_22,inline_bron_btn_22_23,inline_bron_btn_23_00)

inline_pay_btn = InlineKeyboardMarkup(row_width=1)
inline_pay_btn.add(inline_pay_1h_btn,inline_back_menu)



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
        await bot.send_message(chat_id=query.message.chat.id, text=f"Вы хотите забронироваить поля под id:{bron_id}\n\nПожалуйста выберите время:",reply_markup=button_brom_menu)
        
    if data_str.find('h') != -1:

        await bot.send_message(chat_id=query.message.chat.id, text=f"Для бронирования поли пожалуйста оплатите переходя по ссылке ниже:",reply_markup=inline_pay_btn)

    if data_str == 'menu':
         await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id)
         await bot.delete_message(chat_id=query.message.chat.id, message_id=query.message.message_id-1)

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True
    )