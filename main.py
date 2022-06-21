#import
from aiogram import *
from aiogram.types import *
from db import *
#from m import *
import wikipedia
import asyncio

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=bot_token)
m = Dispatcher(bot)


button1 = InlineKeyboardButton(text="button1", callback_data="button1")
button2 = InlineKeyboardButton(text="button2", callback_data="button2")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).add("👋 Hello!", "Youtube")


keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_phone = KeyboardButton(text="Send phone", request_contact=True)
keyboard.add(button_phone)


text = """

This is registration bot of IT School!
Click /list for registration for course.
/list
👇👇👇👇👇
author: @MuzaffarSmartBoy 😎😎😎😎😎
Channel: @MuzaffarSmartBoyChannel 
Group: @MuzaffarSmartBoyGroup
👆👆👆👆👆
"""

clist = """

Dasturlash:
/python - Python
/javadroid - Java Android
/web - Web

Grafika:
/photoshop - PhotoShop
/coreldraw - Corel Draw
/illustrator - illustrator 

Arxitektura:
/3dmax - 3DMax
/autocad - AutoCad

Roboto texnika:
/robotech - Roboto Texnika

Qoshimcha darslar:
/iteng - IT English
/compsavod - Computer Savodxonligi

"""





@m.message_handler(commands=['help'])
async def random_answer(message: Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)


@m.message_handler(commands=['start', 'help'])
async def welcome(message: Message):
    await message.reply(text, reply_markup=keyboard1)

@m.message_handler(commands=['admin'])
async def _(message: Message):
   await message.reply('@MuzaffarSmartBoy')
   

@m.message_handler(commands=['number'])
async def phone(message):
    await message.answer('Phone number', reply_markup=keyboard)


@m.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        print(message.contact)



txt = ["salom", "hello", "hi", "hey", "qalesiz", "qalesan"]

# @m.message_handler()
# async def _(message: Message):
#
#     if message.text in txt:
#         await message.reply("assalomu alaykum!")




@m.message_handler(commands=['img'])
async def _(message: Message):

    await message.answer_photo(photo="m/m.jpg")


@m.message_handler(commands=['video'])
async def _(message: Message):

    await bot.send_video(chat_id=message.chat.id, video=open("m/m.mp4", "rb"))


@m.message_handler(commands=['audio'])
async def _(message: Message):

    await bot.send_audio(chat_id=message.chat.id, audio=open("m/m.mp3", "rb"))


@m.message_handler(commands=['image'])
async def _(message: Message):

    await bot.send_photo(chat_id=message.chat.id, photo=open("m/m.jpg", "rb"))



# @m.message_handler(commands=['file'])
# async def _(message: Message):
#
#     await bot.send_file(file_type="pdf", file=open("C:/Users/FOYDALANUVCHI/Desktop/m.pdf", "rb"))


@m.message_handler(commands=['file'])
async def _(message: Message):

    file = open("m/m.pdf", "rb")
    await message.reply_document(file)


# @m.message_handler()
# async def _(message: Message):
#     try:
#         wikipedia.set_lang("uz")
#         wikitxt = wikipedia.summary(message.text)
#         await message.reply(wikitxt)
#     except:
#         await message.reply(f"Sorry, i didn't find about {message.text}!")


#IT School

@m.message_handler(commands=['list'])
async def _(message: Message):

    await message.answer(clist)







#echo command (args)

from aiogram.dispatcher.filters import Command

@m.message_handler(commands="echo", commands_prefix="/!.")
async def echo_command(message: Message, command: Command.CommandObj):
    if message.get_args() or command.args:
        await message.answer(message.get_args())
        await message.answer(command.args)
        print(command.args)
    else:
        await message.answer("Iltimos, commandadan keyin ma'lumot kiriting! \n(exp: /echo type anything).")








#edit

@m.message_handler(commands='edit')
async def _(message: Message):

    msg = await message.answer("Starting...")
    for i in range(6):
        
        await asyncio.sleep(1)
        await msg.edit_text(i)
    await message.answer("Finished!")




#list

clist = """

Dasturlash:
/python - Python
/javadroid - Java Android
/web - Web

Grafika:
/photoshop - PhotoShop
/coreldraw - Corel Draw
/illustrator - illustrator

Arxitektura:
/3dmax - 3DMax
/autocad - AutoCad

Roboto texnika:
/robotech - Roboto Texnika

Qoshimcha darslar:
/iteng - IT English
/compsavod - Computer Savodxonligi

"""


#functions
def name(message):
    bot.send_message("Please, Send me your name: ")




@m.message_handler(commands=['python'])
async def _(message: Message):

    await message.answer("You selected python!")

    name()









# @m.callback_query_handler(text=["button1", "button2"])
# async def random_value(call: CallbackQuery):
#     if call.data == "button1":
#         await call.message.answer('hi')
#     if call.data == "button2":
#         await call.message.answer('hi')
#     await call.answer()


#Run Code
print('Bot is Running...!')
executor.start_polling(m, skip_updates=True)


