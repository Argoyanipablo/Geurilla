from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from config import ASSISTANT_NAME as bn


@Client.on_callback_query(filters.regex("help"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{bn} to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /vstream (reply to video) to start streaming.
6.) type /vstop to end the video streaming.

📝 **note: stream & stop command can only be executed by group admin only!**

⚡ __ᴘᴀʀᴛ ᴏꜰ ᴢᴀɪᴅ  ᴛᴇᴀᴍ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ʙᴀᴄᴋ", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Hello there, I am a telegram video streaming bot.**\n\n💭 **I was created to stream videos in group video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
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
                             "👩🏻‍💻 ᴅᴇᴠ", url="https://t.me/Timesisnotwaiting")
                       ],[
                          InlineKeyboardButton(
                             "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/Zaid_Support"),
                          InlineKeyboardButton(
                             "🎑 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟꜱ", url="https://t.me/Zaid_Updates")
                       ]]
                    ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **bot information !**

😇 __This bot was created to stream video in telegram group video chats using several methods from Zweb Server.__

💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots.__


__This bot licensed under GNU-GPL 3.0 License__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ʙᴀᴄᴋ", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )

@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""😏 ᴀʟʟ ᴄᴍᴅꜱ ʟɪꜱᴛ:

» /vstream (reply to video or file) - to stream video
» /vstop - end the video streaming
» /song (song name) - download song from YT
» /vsong (video name) - download video from YT
» /lyric (song name) - lyric scrapper

⚡ __ᴘᴀʀᴛ ᴏꜰ ᴢᴀɪᴅ ᴜᴘᴅᴀᴛᴇꜱ__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "ʙᴀᴄᴋ", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
