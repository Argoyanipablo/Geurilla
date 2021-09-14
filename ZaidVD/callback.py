from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Zaid


@Client.on_callback_query(filters.regex("help"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ Bot necə işləyir?:

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
                             "Qrupa Əlavə Et", callback_data="help")
                       ],[
                          InlineKeyboardButton(
                             "😈 Söhbət Qrupumuz", url="https://t.me/dark_sohbet")
                       ],[
                          InlineKeyboardButton(
                             "👀 Botun əmrləri", callback_data="cblist")
                       ],[
                          InlineKeyboardButton(
                             "Sahiblə əlaqə", url="https://t.me/ABISHOV_27")
                       ],[
                          InlineKeyboardButton(
                             "Developer", url="https://t.me/YusifinBiosu"),
                          InlineKeyboardButton(
                             "🎑 Mənbə", url="https://t.me/YusifinBiosu")
                       ]]
                    ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **bot haqqında !**

😇 __Bot vasitəsilə Qruplarda Səsli Söhbət zamanı mahnını klipiylə bərabər izləyə, canlı yayımlar izləyə üstəlik filmlərədə baxa bilərsiniz.__

💡 __Xoş izləmələr, Xoş dinləmələr🤗❤.__


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
    f"""😏 Botu işə salma qaydası:

» /vplay (youtube linkinə yanıt verin yt link/canı yayın link url) - səslidə linkə yanıt verdiyiniz videonu, canlı yayımı , filmi və s. açar
» /vstop - botu dayandırar
» /song (mahnı adı) - istədiyiniz mahnını yükləyər
» @vid (video adı) - axtardığınız videonun youtube linkini hazırlayar
» /vjoin - asistantı qrupa dəvət edər
» /vleave - asistantı qrupdan çıxarar

🔰 Əlavə əmrlər:

» /tts (mətnə yanıt verin) - yanıt verdiyiniz mətni səsə çevirər
» /alive - botun işləyib işləmədiyini yoxlayar
» /ping - botun pingini ölçər
» /uptime - botun işləmə vəziyyətini yoxlayar
» /stats - botun sistem mılumatlarını yoxlayar

💡 Sahib əmrləri:

» /rmd - botla yüklənən bütün medianı silər
» /rmw - yüklənən bütün raw fayllarını silər
» /leaveall - asistantı bütün qrupçarfan çıxarar

⚡ __@ABISHOV_27 tərəfindən hazırlandı__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "Çıxış", callback_data="cbstart")
      ]]
    ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
