from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    FSInputFile,
)
from forms.user import Form
from aiogram.fsm.context import FSMContext
from aiogram import Bot
import aiohttp
import aiosqlite
import asyncio

router = Router()


#----------------------------

# def get_main_reply_keyboard():
#     keyboard = ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="/about")],
#             [KeyboardButton(text="Start"), KeyboardButton(text="Help")]
#         ],
#         resize_keyboard=True,
#         is_persistent=True)
#     return keyboard

# def get_main_inline_keyboard():
#     keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text="Open site", url="https://google.com")],
#             [InlineKeyboardButton(text="More", callback_data="info_more")]
#         ]
#     )
#     return keyboard

# @router.callback_query(lambda c: c.data == "info_more")
# async def proccess_more_info(callback: CallbackQuery):
#     await callback.message.answer("There is more info")
#     await callback.answer()

#---------------

# @router.message(Command("start"))
# @router.message(F.text.lower() == "start")
# async def start(message: Message):
#     await message.answer(
#         "Hello! I'm *simple* bot _for_ you\n\nSend /help for help",
#         parse_mode="Markdown")
    
# @router.message(Command("help"))
# async def help(message: Message):
#     await message.answer(
#         "Commands:\n<b>/start</b> - start bot\n<i>/help</i> - <a href='https://google.com'>commands</a> list\n/about - about bot",
#         parse_mode="HTML",
#         reply_markup=get_main_reply_keyboard())
    
# @router.message(Command("about"))
# async def about(message: Message):
#     await message.answer(
#         f"About bot. Your name: {message.from_user.first_name}", reply_markup=get_main_inline_keyboard())
    
# @router.message()
# async def text(message: Message):
#     await message.answer("Text message")

# @router.message(Command("start"))
# async def start(message: Message, state: FSMContext):
#     await message.answer("Your name: ")
#     await state.set_state(Form.name)
    
# @router.message(Command("cancel"))
# async def cancel_form(message: Message, state: FSMContext):
#     await state.clear()
#     await message.answer("Process canceled")
#-----------
    
# @router.message(Form.name, F.text)
# async def process_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer("Your age: ")
#     await state.set_state(Form.age)

# @router.message(Form.age, F.text)
# async def process_age(message: Message, state: FSMContext):
#     if not message.text.isdigit():
#         await message.answer("Age must be digit")
#         return
#     if int(message.text) < 1 or int(message.text) > 100:
#         await message.answer("Age must between 1 and 100")
#         return
    
#     await state.update_data(age=int(message.text)) 
    
#     await message.answer("Your email: ")
#     await state.set_state(Form.email)

# @router.message(Form.email, F.text)
# async def process_email(message: Message, state: FSMContext):
#     email_text = message.text
#     if "@" not in email_text or "." not in email_text:
#         await message.answer("Invalid email")
#         return
    
#     await state.update_data(email=email_text) 
    
#     data = await state.get_data()
#     name = data["name"]
#     age = data["age"]
#     email = data["email"]
    
#     await message.answer(f"Data collected.\nName: {name}\nAge: {age}\nEmail: {email}")
#     await state.clear()

#---------------------
    
# @router.message(F.photo)
# async def process_photo(message: Message):
#     photo = message.photo[-1]
#     file_id = photo.file_id
    
#     await message.answer(f"You send a photo\n ID photo: <code>{file_id}</code>", parse_mode="HTML")
#     await message.answer_photo(file_id, caption="Here your photo")
    
# @router.message(F.video)
# async def process_video(message: Message):
#     video = message.video
#     file_id = video.file_id
#     duration = video.duration
    
#     await message.answer(f"You send a video\nID video: <code>{file_id}</code>\nVideo duration: <code>{duration}</code>", parse_mode="HTML")
#     await message.answer_video(file_id, caption="Here your video")
    
# @router.message(F.animation)
# async def process_animation(message: Message):
#     animation = message.animation
    
#     await message.answer(f"You send a animation\n ID animation: <code>{animation.file_id}</code>", parse_mode="HTML")
#     await message.answer_animation(animation.file_id, caption="Here your animation")
    
# @router.message(F.document)
# async def process_document(message: Message, bot: Bot):
#     document = message.document
#     file_id = document.file_id
    
#     file = await bot.get_file(file_id)
#     file_path = file.file_path
#     local_path = f"downloads/{document.file_name}"
    
#     await bot.download_file(file_path=file_path, destination=local_path)
#     await message.answer("File saved")
    
# @router.message(Command("file"))
# async def send_file(message: Message):
#     file = FSInputFile('files/example.txt')
    
#     await message.answer_document(file)
#------------------

# async def get_product(product_id):
#     url = f"https://fakestoreapi.com/products/{product_id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             if resp.status == 404:
#                 return None
            
#             data = await resp.json()
#             return data

# @router.message(Command("start"))
# @router.message(F.text.lower() == "start")
# async def start(message: Message):
#     await message.answer(
#         "Hello! I'm simple bot for you\n\nUse command: /product ID. Example: <b>product 1</b>",
#         parse_mode="HTML")
    
# @router.message(Command("product"))
# @router.message(F.text.lower() == "product")
# async def get_product_cmd(message: Message):
#     parts = message.text.strip().split()
#     if len(parts) != 2:
#         await message.answer("Use: /product 1")
#         return
    
#     product_id = parts[1]
#     if not product_id.isdigit():
#         await message.answer("ID must be a number")
#         return
    
#     await message.answer(f"Searching product with ID: {product_id}")
    
#     try:
#         product = await get_product(int(product_id))
#     except Exception:
#         await message.answer("Cant connect to server")
#         return

#     if product is None:
#         await message.answer("There is no such a product")
#         return
    
#     title = product.get("title", "Unnamed")
#     price = product.get("price", "-")
#     desc = product.get("description", "No description")
#     category = product.get("category", "No category")
#     image = product.get("image")
    
#     text = (
#         f"<b>{title}</b>\n\n"
#         f"Category <i>{category}</i>\n"
#         f"Price: <b>{price}$</b>\n"
#         f"{desc}"
#     )
    
#     # if image:
#     #     await message.answer_photo(photo=image, caption=text, parse_mode="HTML")
#     # else:
#     #     await message.answer(text, parse_mode="HTML")

#     photo = FSInputFile("no_image.png")
#     await message.answer_photo(photo=photo, caption=text, parse_mode="HTML")

#---------------------------------------
# DB_NAME = "itproger.sql"

# async def init_db():
#     async with aiosqlite.connect(DB_NAME) as db:
#         await db.execute("""
#             CREATE TABLE IF NOT EXISTS users(
#                 id INTEGER PRIMARY KEY, 
#                 full_name TEXT,
#                 age INTEGER
#             )
#                          """)
#         await db.commit()
        
# async def add_user(full_name, age):
#     async with aiosqlite.connect(DB_NAME) as db:
#         await db.execute("""INSERT INTO users(full_name, age) VALUES(?,?)""", (full_name, age))
#         await db.commit()
        
# async def get_users():
#     async with aiosqlite.connect(DB_NAME) as db:
#         cursor = await db.execute("""SELECT full_name, age FROM users""")
#         result = await cursor.fetchall()
#         return result
    
# @router.message(Command("start"))
# @router.message(F.text.lower() == "start")
# async def start(message: Message):
#     await init_db()
#     await message.answer(
#         "Hello! I'm simple bot for you\n\nUse command: /reg AGE.",
#         parse_mode="HTML")

# @router.message(Command("reg"))
# @router.message(F.text.lower() == "reg")
# async def reg(message: Message):
#     parts = message.text.strip().split()
    
#     if len(parts) != 2 or not parts[1].isdigit():
#         await message.answer("Invalid command")
#         return
    
#     await add_user(message.from_user.full_name, int(parts[1]))
    
#     await message.answer(
#         "All done",
#         parse_mode="HTML")
    
# @router.message(Command("users"))
# @router.message(F.text.lower() == "users")
# async def users(message: Message):
#     users = await get_users()
    
#     if not users:
#         await message.answer("There are no users in database")
#         return
    
#     text = "Users in database:\n\n"
#     for full_name, age in users:
#         text += f"- {full_name} - <code>{age}</code>\n"
        
#     await message.answer(text, parse_mode="HTML")
#-------------------------------------------

subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user_id in list(subscribers):
                try:
                    await bot.send_message(user_id, "Your common message")
                except Exception:
                    pass
                
        await asyncio.sleep(10)

@router.message(Command("start"))
@router.message(F.text.lower() == "start")
async def start(message: Message):
    await message.answer(
        "Hello!\n"
        "I can help you with subscribes\n\n"
        "Commands: \n"
        "/subscribe - subscribe to notifications\n"
        "/unsubscribe\n"
        "/subscribers - subscribers list",
        parse_mode="HTML")
    
@router.message(Command("subscribe"))
@router.message(F.text.lower() == "subscribe")
async def subscribe(message: Message):
    user_id = message.from_user.id
    subscribers.add(user_id)
    await message.answer("You subscribed")
    
@router.message(Command("unsubscribe"))
@router.message(F.text.lower() == "unsubscribe")
async def unsubscribe(message: Message):
    user_id = message.from_user.id
    subscribers.discard(user_id)
    await message.answer("You unsubscribed")
    
@router.message(Command("subscribers"))
@router.message(F.text.lower() == "subscribers")
async def subscribers_cmd(message: Message):
    if not subscribers:
        await message.answer("No subscribers")
        return
    
    text = "Subscribers:\n"
    for uid in subscribers:
        text += f"{uid}\n"
    await message.answer(text)