from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



def navigator_buttons(messega_id):
    bron_id = messega_id
    messega_id = int(messega_id) + 1
    messega_id_back = messega_id -2
    
    count_id = messega_id - 2

    if messega_id == 11:
        messega_id = 2

    if messega_id == 3:
        messega_id_back = 10

    inline_btn_next = InlineKeyboardButton("▶️", callback_data=f"next_{messega_id}")
    inline_btn_back = InlineKeyboardButton("◀️", callback_data=f"back_{messega_id_back}")
    inline_btn_bron = InlineKeyboardButton('Забронировать поля 🔒', callback_data=f"bron_{bron_id}")

    count_bron = InlineKeyboardButton(f"{count_id}/9", callback_data=f"next_{messega_id}")

    button_navigator = InlineKeyboardMarkup()
    button_navigator.add(inline_btn_back, inline_btn_next)
    button_navigator.row(inline_btn_bron)
    button_navigator.row(count_bron)

    return button_navigator

def callbeck_bron_data(date):
    id = date.split("_")[2]
    date = date.split("_")[0]
    
    text = f"Платеж к оплату\n\nid: {id}\nДата: 21.11.2023\nВремя: {date}\n\nК оплате: 15000 тенге"

    return text

def button_bron_menu(date):
    id = date.split("_")[1]
    inline_bron_date = InlineKeyboardButton(f"21-11", callback_data='21-11')
    inline_bron_date_back = InlineKeyboardButton('<-', callback_data='date_back')
    inline_bron_date_next = InlineKeyboardButton('->', callback_data='date_next')

    inline_bron_btn_09_10 = InlineKeyboardButton("09-10 🔒", callback_data=f"09-10_h_{id}")
    inline_bron_btn_10_11 = InlineKeyboardButton("10-11 🔒", callback_data=f"10-11_h_{id}")
    inline_bron_btn_11_12 = InlineKeyboardButton("11-12 🔒", callback_data=f"11-12_h_{id}")
    inline_bron_btn_12_13 = InlineKeyboardButton("12-13 🔒", callback_data=f"12-13_h_{id}")
    inline_bron_btn_13_14 = InlineKeyboardButton("13-14", callback_data=f"13-14_h_{id}")
    inline_bron_btn_14_15 = InlineKeyboardButton("14-15", callback_data=f"14-15_h_{id}")
    inline_bron_btn_15_16 = InlineKeyboardButton("15-16", callback_data=f"15-16_h_{id}")
    inline_bron_btn_16_17 = InlineKeyboardButton("16-17 🔒", callback_data=f"16-17_h_{id}")
    inline_bron_btn_17_18 = InlineKeyboardButton("16-17 🔒", callback_data=f"17-18_h_{id}")
    inline_bron_btn_18_19 = InlineKeyboardButton("18-19", callback_data=f"18-19_h_{id}")
    inline_bron_btn_19_20 = InlineKeyboardButton("19-20", callback_data=f"19-20_h_{id}")
    inline_bron_btn_20_21 = InlineKeyboardButton("20-21", callback_data=f"20-21_h_{id}")
    inline_bron_btn_21_22 = InlineKeyboardButton("21-22", callback_data=f"21-22_h_{id}")
    inline_bron_btn_22_23 = InlineKeyboardButton("22-23", callback_data=f"22-23_h_{id}")
    inline_bron_btn_23_00 = InlineKeyboardButton("22-23", callback_data=f"23-00_h_{id}")

    inline_bron_btn = InlineKeyboardButton("Забронироваить", callback_data='bron')

    button_brom_menu1 = InlineKeyboardMarkup(row_width=3)
    button_brom_menu1.add(inline_bron_date_back, inline_bron_date, inline_bron_date_next,   
                    inline_bron_btn_09_10,inline_bron_btn_10_11,inline_bron_btn_11_12,
                     inline_bron_btn_12_13,inline_bron_btn_13_14,inline_bron_btn_14_15,
                     inline_bron_btn_15_16,inline_bron_btn_16_17,inline_bron_btn_17_18,
                     inline_bron_btn_18_19,inline_bron_btn_19_20,inline_bron_btn_20_21,
                     inline_bron_btn_21_22,inline_bron_btn_22_23,inline_bron_btn_23_00,
                     inline_bron_btn )
    
    return button_brom_menu1