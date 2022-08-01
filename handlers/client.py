from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from keyboards import client_kb

# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"Салам алейкум {message.from_user.full_name}",
                           reply_markup=client_kb.start_murkup)

# @dp.message_handler(commands=['meme'])
async def meme_handler(message: types.Message):
    photo = open('media/123.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)

# @dp.message_handler(commands=['quiz'])
async def quiz_handler(message: types.Message):
    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next', callback_data='button_call_1')
    murkup.add(button_call_1)
    question = "За сколько хочешь меня купить?"
    answers = ["15к сом", "10 сом", "Бесплатно"]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type ='quiz',
        correct_option_id=2,
        explanation='Размечтался Не продаюсь',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=murkup,


    )




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(meme_handler, commands=['meme'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
