import asyncio
from os import environ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))


ALL_PIC = [
 "https://telegra.ph/file/6cff45eb89df1648be888.jpg",
 "https://telegra.ph/file/c283bf783cc9ba943949d.jpg",
 "https://telegra.ph/file/3ac4981982a84f8599030.jpg",
 "https://telegra.ph/file/a8c47c80387d02ed58eaf.jpg"
]


@User.on_message(filters.command("start")) 
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f""" 𝙃𝙞 {message.from_user.mention} 𝙞'𝙢 𝙖 𝙬𝙤𝙧𝙠 𝙞𝙣 𝙥𝙧𝙤𝙜𝙧𝙚𝙨𝙨 𝙗𝙤𝙩 𝙩𝙝𝙞𝙨 𝙗𝙤𝙩 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙖𝙘𝙩𝙞𝙫𝙚 𝙨𝙤𝙤𝙣 𝙥𝙡𝙚𝙖𝙨𝙚 𝙟𝙤𝙞𝙣 𝙤𝙪𝙧 𝙢𝙖𝙞𝙣 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙜𝙧𝙤𝙪𝙥.
❓ WHICH ARE THE COMMANDS? ❓
Press /help to see all the commands and how they work!
https://t.me/Uncanny_Movies01 """,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("➕𝖠𝖣𝖣 𝖳𝖮 𝖸𝖮𝖴𝖱 𝖦𝖱𝖮𝖴𝖯➕", url=f"https://t.me/LucasHood099_Bot?startgroup=true")
            ],[
            InlineKeyboardButton("𝖧𝖾𝗅p⚙️", url="t.me/GroupHelpBot"),
            InlineKeyboardButton("𝖢𝗈𝗇𝗍𝖺𝖼𝗍 𝖴𝗌💬", url="t.me/LucasHood_099")
            ],[
            InlineKeyboardButton("𝖦𝗋𝗈𝗎𝗉👥", url="https://t.me/Uncanny_Group"),
            InlineKeyboardButton("𝖢𝗁𝖺𝗇𝗇𝖾𝗅📎", url="t.me/Uncanny_Movies01")
            ]]
            )
        )

User = Client(session_name=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(session_name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.message_id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
