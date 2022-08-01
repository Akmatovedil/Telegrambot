from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton('/start')
meme_button = KeyboardButton('/meme')
quiz_button = KeyboardButton('/quiz')
location_button = KeyboardButton('Share lovation', request_location=True)
info_button = KeyboardButton('Share info', request_contact=True)

start_murkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_murkup.row(start_button, meme_button, quiz_button)
start_murkup.add(location_button, info_button)

cancel_button = KeyboardButton('Cancel')
cancel_murkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(cancel_button)
