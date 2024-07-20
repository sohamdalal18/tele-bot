import os
import logging
from aiogram import Bot, Dispatcher, executor, types
import openai
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_BOT_token")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI API client
openai.api_key = OPENAI_API_KEY

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Handle start and help commands
@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with '/start' or '/help' command
    """
    await message.reply("Hi\nThis is Dastgeer!\nPowered by aiogram and OpenAI. ")

# Handle messages and generate a response using OpenAI API
@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return a response from the OpenAI API
    """
    response = openai.Completion.create(
        model="text-davinci-001",
        prompt=message.text,
        temperature=0.5,
        max_tokens=100
    )
    await message.answer(response.choices[0].text)

# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)