from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import Zaid
from helpers.decorators import sudo_users_only
from helpers.filters import command

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
      await m.reply(f"🥴 Merhaba ben gruplarınızda video izleme ve muzik dinleme botuyum.\n\n💭 Beni grubuna eklersen sevinirim .\n\n❔. komutlarımı assagidaki butondan öğrenebilirsiniz👇🏻",
                    reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "Əlavə et", url="https://t.me/{Zaid.BOT_USERNAME}?startgroup=true")
                       ],[
                          InlineKeyboardButton(
                             "😈 Sahibim", url="https://t.me/Doguturkblogu")
                       ],[
                          InlineKeyboardButton(
                             "👀 Botun əmrləri", callback_data="cblist")
                       ],[
                          InlineKeyboardButton(
                             "Grubumuz 🇹🇷", url="https://t.me/kizilsancakglobal")
                       ],[
                          InlineKeyboardButton(
                             "Reklam", url="https://t.me/Gstilki1453"),
                          InlineKeyboardButton(
                             "🎑 Developer", url="https://t.me/adsizimlores")
                       ]]
                    ))
   else:
      await m.reply("**✨ Bot işləyir qadanalım... ✨**",
                          reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "Qrupumuz", url="https://t.me/kizilsancakglobal")
                       ],[
                          InlineKeyboardButton(
                             "🔥 Reklam", url="https://t.me/GsTilki1453")
                       ],[
                          InlineKeyboardButton(
                             "📚 DESTEK", url="https://t.me/kizilsancakglobal")
                       ]]
                    )
                    )

@Client.on_message(command(["alive", f"alive@{Zaid.BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"""✅ **Bot işə salınır**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ Grup", url=f"https://t.me/kizilsancakglobal"
                    ),
                    InlineKeyboardButton(
                        "📣 Sahib", url=f"https://t.me/Gstilki1453"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{Zaid.BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(_, m: Message):
    sturt = time()
    m_reply = await m.reply_text("Zaid...")
    delta_ping = time() - sturt
    await m_reply.edit_text(
        "🏓 ℙ𝕠𝕟𝕘`!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{Zaid.BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "🤖 Bot statusu 🤖\n\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
