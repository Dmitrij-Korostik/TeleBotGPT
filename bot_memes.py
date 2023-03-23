import random
import json

from aiogram import Bot, Dispatcher, executor, types
from get_memes_for_api import get_memes
from get_neiro_memes import get_neiro_memes

token = '6014401350:AAFE9tJCfIl26fwtfjPoFusc10Uzg1MLLnk'
bot = Bot(token=token)
disp = Dispatcher(bot)



@disp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Нейросеть")
    button_2 = types.KeyboardButton(text="Мем")

    keyboard.add(button_1)
    keyboard.add(button_2)

    await message.answer(
        "Для того что получить мем нажмите на кнопку!\n",
        reply_markup=keyboard)


@disp.message_handler(lambda message: message.text == "Нейросеть")
async def parser_memes(message: types.Message):
    with open('neiro.json', 'r') as file:
        mem = random.choice(json.load(file)['img'])
    await bot.send_photo(message.chat.id, mem)

@disp.message_handler(lambda message: message.text == "Мем")
async def parser_memes(message: types.Message):
    with open('memes.json', 'r') as file:
        mem = random.choice(json.load(file)['image'])
    await bot.send_photo(message.chat.id, mem)



if __name__ == '__main__':
    get_memes("https://api.memegen.link/images")
    get_neiro_memes()
    executor.start_polling(disp, skip_updates=True)