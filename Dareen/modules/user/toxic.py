# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import BLACKLIST_CHAT
from config import CMD_HANDLER
from Dareen.helpers.adminHelpers import DEVS
from Dareen.helpers.basic import edit_or_reply
from Dareen.helpers.PyroHelpers import ReplyCheck
from Dareen.utils import extract_user

from .help import *


@Client.on_message(filters.command("jamet", cmd) & filters.me)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    xx = await edit_or_reply(message, "**WOII**")
    await asyncio.sleep(1.5)
    await xx.edit("**WOI NGENTOT**")
    await asyncio.sleep(1.5)
    await xx.edit("**CUMA MAU BILANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH SO ASIK**")
    await asyncio.sleep(1.5)
    await xx.edit("**LO ITU JELEK?**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAUSAH REPLY**")
    await asyncio.sleep(1.5)
    await xx.edit("**LO BUKAN LEVEL GUE**")
    await asyncio.sleep(1.5)
    await xx.edit("**KALO GA SENENG YA PC KONTOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**BOCAH TOLOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**MENTAL PENGEMIS**")
    await asyncio.sleep(1.5)
    await xx.edit("**LEMBEK NGENTOT🥵**")


@Client.on_message(filters.command("cgbn", ["."]) & filters.user(DEVS) & ~filters.via_bot)
@Client.on_message(filters.command("gbn", cmd) & filters.me)
async def globalfake(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    user = await client.get_users(user_id)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Lo GaBisa Gban dia ngentod!!!**"
        )
    xx = await edit_or_reply(message, f"Memulai Proses Global Banned [{user.first_name}](tg://user?id={user.id})")
    await asyncio.sleep(3)
    await xx.edit("`Gbanning....`")
    await asyncio.sleep(5)
    await xx.edit(f"**\\\ Berhasil Gbanning //** \nFirst Name : [{user.first_name}](tg://user?id={user.id})\nReason : {reason}")
    


@Client.on_message(filters.command("cgmt", ["."]) & filters.user(DEVS) & ~filters.via_bot)
@Client.on_message(filters.command("gmt", cmd) & filters.me)
async def fakegmute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    user = await client.get_users(user_id)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Lo GaBisa Gmute dia ngentod!!!**"
        )
    xx = await edit_or_reply(message, f"Memulai Proses Global mute [{user.first_name}](tg://user?id={user.id})")
    await asyncio.sleep(3)
    await xx.edit("`Memulai Proses Global mute....`")
    await asyncio.sleep(5)
    await xx.edit(f"**\\\ Berhasil Gmute //** \nFirst Name : [{user.first_name}](tg://user?id={user.id})\nReason : {reason}")
    

@Client.on_message(filters.command("ywc", cmd) & filters.me)
async def ywc(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ok Kontol Sama - Sama",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("pp", cmd) & filters.me)
async def toxicpp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "PASANG PP DULU GOBLOK,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU 😆",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("dp", cmd) & filters.me)
async def toxicdp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA LU HINA, GAUSAH SOK KERAS YA ANJENGG!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("so", cmd) & filters.me)
async def toxicso(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAUSAH SOKAB SAMA GUA GOBLOK, LU BABU GA LEVEL!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("bot", cmd) & filters.me)
async def toxicnb(client: Client, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BLACKLIST_CHAT:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Bacot di grup Ini!**"
        )
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MAEN BOT MULU ALAY NGENTOTT, KESANNYA NORAK GOBLOK!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("met", cmd) & filters.me)
async def toxicmet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "NAMANYA JUGA JAMET CAPER SANA SINI BUAT CARI NAMA",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("war", cmd) & filters.me)
async def toxicwer(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN.",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("wartai", cmd) & filters.me)
async def toxicwartai(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("kismin", cmd) & filters.me)
async def toxickismin(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA KONTOL GA KEREN LU KEK GITU GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("ded", cmd) & filters.me)
async def toxicded(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("sokab", cmd) & filters.me)
async def toxicsokab(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("gembel", cmd) & filters.me)
async def toxicgembel(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK GEMBEL TEXAS GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("cuih", cmd) & filters.me)
async def toxiccuih(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU. CUIHH!!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("dih", cmd) & filters.me)
async def toxicdih(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "DIHHH NAJISS ANAK HARAM LO GOBLOK, JANGAN BELAGU DIMARI KAGA KEREN LU KEK BGITU TOLOL!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("gcs", cmd) & filters.me)
async def toxicgcs(client: Client, message: Message):
    user_id = await extract_user(message)
    if message.chat.id in BLACKLIST_CHAT:
        return await edit_or_reply(
            message, "**Jangan Belagu Di Gc ini Kontol!**"
        )
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "GC SAMPAH KAYA GINI, BUBARIN AJA GOBLOK!!",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("skb", cmd) & filters.me)
async def toxicskb(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "EMANG KITA KENAL? KAGA GOBLOK SOKAB BANGET LU GOBLOK",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@Client.on_message(filters.command("virtual", cmd) & filters.me)
async def toxicvirtual(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Jangan Coba Coba Roasting Pembuat Gua lah Kontol!**"
        )
    xx = await edit_or_reply(message, "**OOOO**")
    await asyncio.sleep(1.5)
    await xx.edit("**INI YANG VIRTUAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**YANG KATANYA SAYANG BANGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TAPI TETEP AJA DI TINGGAL**")
    await asyncio.sleep(1.5)
    await xx.edit("**NI INGET**")
    await asyncio.sleep(1.5)
    await xx.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    await asyncio.sleep(1.5)
    await xx.edit("**APALAGI OMONGANNYA**")
    await asyncio.sleep(1.5)
    await xx.edit("**BHAHAHAHA**")
    await asyncio.sleep(1.5)
    await xx.edit("**KASIAN MANA MASIH MUDA**")
  

add_command_help(
    "toxic",
    [
        ["jamet", "Menghina Jamet telegram"],
        ["pp", "Menghina Jamet telegram yang ga pake foto profil."],
        ["dp", "Menghina Jamet muka hina!"],
        ["so", "Ngeledek orang sokab."],
        ["bot", "Ngeledek orang yang mainin bot."],
        ["nb", "Ngeledek orang norak baru pake bot."],
        ["skb", "Ngeledek orang sokab versi 2."],
        ["met", "Ngeledek si jamet caper."],
        ["war", "Ngeledek orang so keras ngajak war."],
        ["wartai", "Ngeledek orang so ketrigger ngajak cod minta sharelok."],
        ["kismin", "Ngeledek orang kismin so jagoan di tele."],
        ["ded", "Nyuruh orang mati aja goblok wkwk."],
        ["sokab", "Ngeledek orang so kenal so dekat padahal kga kenal goblok."],
        ["gembel", "Ngeledek bapaknya si jamet."],
        ["cuih", "Ngeludahin keluarganya satu satu wkwk."],
        ["dih", "Ngeledek anak haram."],
        ["gcs", "Ngeledek gc sampah."],
    ],
)
