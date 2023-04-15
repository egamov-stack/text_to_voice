
# API_TOKEN = '6119831273:AAF1kWtW8Q9rndSDJyNtzU9H2UOVXToDs0o'


import asyncio, os
import aiogram
from gtts import gTTS

# create an instance of AIogram bot
bot = aiogram.Bot(token='6119831273:AAF1kWtW8Q9rndSDJyNtzU9H2UOVXToDs0o')
dp = aiogram.Dispatcher(bot)

# define a function to convert text to speech
async def text_to_speech(message):
    # extract text from message
    text = message.text

    # generate the text-to-speech audio file
    tts = gTTS(text=text, lang='ru')
    tts.save('output.mp3')

    # send the audio file to the user
    with open('output.mp3', 'rb') as f:
        await bot.send_audio(chat_id=message.chat.id, audio=f, title='Text-to-Speech')

    # remove the audio file from disk
    os.remove('output.mp3')

# register the message handler
dp.register_message_handler(text_to_speech)

# start the AIogram bot
async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())

