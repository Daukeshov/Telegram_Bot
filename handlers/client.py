from aiogram import types, Dispatcher
from create_bot import bot
from keyboards  import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps:/t.me/Madi_Pizza')


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message : types.Message):
        await bot.send_message(message.from_user.id, 'Понедельник-Воскресенье с 9:00 до 20:00')


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
        await bot.send_message(message.from_user.id, 'ул. Колбасная, 15', reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])