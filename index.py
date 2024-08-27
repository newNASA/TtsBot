import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("Bot_Token")
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Botimizga xush kelibsiz menga matn tashlang men sizga uni ovozga aylantirib beraman")
    
@dp.message()
async def ConvertAudio(message: types.Message):
    text = message.text
    tts = gTTS(text=text, lang="en")
    tts.save(f"{message.chat.id}.mp3")
    file = types.input_file.FSInputFile(path=f"{message.chat.id}.mp3")
    await message.answer_audio(audio=file)
    
    try:
        os.remove(f"{message.chat.id}.mp3")
    except:
        pass
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())