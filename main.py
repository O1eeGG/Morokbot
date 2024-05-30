import aiogram
import asyncio
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart

bot = aiogram.Bot(token="********") #id токен телеграмм бота
dp = aiogram.Dispatcher()


@dp.message(CommandStart())
async def start(message:aiogram.types.Message):
    await message.answer(text="Введите номер сцены (0-37)")


@dp.message()
async def send_songs(message:aiogram.types.Message):
    name='voice/'+message.text+'.mp3'
    audio = FSInputFile(name)
    await bot.send_audio(message.chat.id, audio)
    await message.answer(text="Ваедите номер сцены (0-37)")


async def work():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(work())
