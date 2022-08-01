from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from config import bot, ADMIN
from datetime import datetime


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMIN:
        await FSMAdmin.photo.set()
        await message.answer(f'Добрый день Админ, отправь фото блюда', reply_markup=client_kb.cancel_murkup)
    else:
        await message.reply("Ты не админ")

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('Как называется блюдо ?')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Опишите блюдо!')

async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("Цена блюда?")

async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"Name: {data['name']}\n"
                                     f"Description: {data['description']}\n\n"
                                     f"Price: {data['price']}")
    await state.finish()
    await message.answer('Регистрация блюда завершина!')

async def cancel_regigistation(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer('Регистрация отменена!')


def register_handlers_fsmanketa(dp: Dispatcher):
    dp.register_message_handler(cancel_regigistation, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_regigistation, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['anketa'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
