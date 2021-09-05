from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Chat, CallbackQuery

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
      await m.reply(f"✨ **Hello there, I am a telegram video streaming bot.**\n\n💭 **I was created to stream videos in group video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ʜᴇʟᴘ", callback_data="help")
                       ],[
                          InlineKeyboardButton(
                             "😈 ᴢᴀɪᴅ ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀᴛ", url="https://t.me/zaid_team1")
                       ],[
                          InlineKeyboardButton(
                             "👀 ᴄᴍᴅꜱ ʟɪꜱᴛ", callback_data="cblist")
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/Itsunknown-12/Zaid-Video-Player")
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/Zaid_Support"),
                          InlineKeyboardButton(
                             "🎑 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟꜱ", url="https://t.me/Zaid_Updates")
                       ]]
                    ))
   else:
      await m.reply("**✨ ᴍɪɴᴇ ᴀꜱꜱɪꜱᴛᴀɴᴛ ᴜɴᴀʙʟᴇ ᴊᴏɪɴ ᴜʀ ɢʀᴏᴜᴘ ᴍᴀᴋᴇ ᴜʀ ᴏᴡɴ ʙᴏᴛ... ✨**",
                          reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Zaid_Updates")
                       ],[
                          InlineKeyboardButton(
                             "🔥 ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/Itsunknown-12/Zaid-Video-Player")
                       ],[
                          InlineKeyboardButton(
                             "📚 ʜᴇʟᴘ ᴀɴᴅ ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/Zaid_Support")
                       ]]
                    )
      )
