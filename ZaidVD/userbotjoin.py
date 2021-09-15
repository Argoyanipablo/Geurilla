# Copyright (C) 2021 Zaid Music
#Ur Motherfucker If U Kang And Don't Give Creadits 🥴 𝙭𝙕𝘼𝙄𝘿

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.filters import command
from helpers.decorators import authorized_users_only, errors
from ZaidVD.videoplayer import app as USER
from config import Zaid


@Client.on_message(command(["vjoin", f"userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def entergroup(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>💡 bunu etmək üçün əvvəlcə məni admin edin !</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "assistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤖: i'm joined here for streaming video on video chat")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>✅ assistant artıq qrupunuzdadır</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 FLOODWAIT ERROR 🔴\n\n Hey {user.first_name} üzgünəm.Assistant qrupa qoşula bilmədi.Assistanın qrupdan ban edilmədiyinə əmin ol ."
        )
        return
    await message.reply_text(
        "<b>✅ assistant qrupa qoşuldu chat</b>",
    )


@Client.on_message(command(["vleave", f"vleave@{Zaid.BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leavegroup(client, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "<b>❌ assistant qrupdan çıxa bilməz.\n\n» yalnızca qrup ayarlarından edə bilərsiz</b>"
        )

        return


@Client.on_message(command(["leaveall", f"leaveall@{Zaid.BOT_USERNAME}"]))
async def outall(client, message):
    if message.from_user.id not in Veez.SUDO_USERS:
        return

    left=0
    failed=0
    lol = await message.reply("🔁 assistant bütün qruplardan çıxdı")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(f"🔁 assistant qrupdan çıxarılır...\n⏳ Təxmini: {left} gözlə.\n\n❌ Alınmadı: {failed} chats.")
        except:
            failed += 1
            await lol.edit(f"🔁 assistant qrupdan çıxarılır...\n⏳ Left: {left} chats.\n\n❌ Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"✅ Left {left} chats.\n\n❌ Failed {failed} chats.")
