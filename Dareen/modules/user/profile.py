# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from Dareen.helpers.basic import edit_or_reply
from Dareen.helpers.PyroHelpers import ReplyCheck
from Daree .utils.misc import extract_user

from .help import *

flood = {}
profile_photo = "Uputt/modules/cache/pfp.jpg"


@Client.on_message(filters.command(["block"], cmd) & filters.me)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    Uputt = await edit_or_reply(message, "`Sabar Lagi blokir Orgil . . .`")
    if not user_id:
        return await message.edit(
            "Berikan User ID/Username atau reply pesan pengguna untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await Uputt.edit("GOBLOK MANA BISA BLOKIR DIRI SENDIRI.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil Memblokir Anak Kontol Ini** {umention}")


@Client.on_message(filters.command(["unblock"], cmd) & filters.me)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    Uputt = await edit_or_reply(message, "`Sabar lagi Buka Blokir Orang Tolol . . .`")
    if not user_id:
        return await message.edit(
            "Berikan User ID/Username atau reply pesan pengguna untuk membuka blokir."
        )
    if user_id == client.me.id:
        return await Uputt.edit("anda stress harap segera minum obat.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Berhasil Membuka Blokir Anak kontol Ini ✌** {umention}")


@Client.on_message(filters.command(["setname"], cmd) & filters.me)
async def setname(client: Client, message: Message):
    Dareen = await edit_or_reply(message, "`Sabar Lagi Ganti Nama. . .`")
    if len(message.command) == 1:
        return await Dareen.edit(
            "Berikan teks untuk ditetapkan sebagai nama telegram anda."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await Dareen.edit(f"**Berhasil Mengubah Nama Telegram anda Menjadi** `{name}`")
        except Exception as e:
            await Dareen.edit(f"**ERROR:** `{e}`")
    else:
        return await Dareen.edit(
            "Berikan teks untuk ditetapkan sebagai nama telegram anda."
        )


@Client.on_message(filters.command(["setbio"], cmd) & filters.me)
async def set_bio(client: Client, message: Message):
    Dareen = await edit_or_reply(message, "`Processing . . .`")
    if len(message.command) == 1:
        return await Dareen.edit("Berikan teks untuk ditetapkan sebagai bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await Dareen.edit(f"**Berhasil Mengubah BIO anda menjadi** `{bio}`")
        except Exception as e:
            await Dareen.edit(f"**ERROR:** `{e}`")
    else:
        return await Dareen.edit("Berikan teks untuk ditetapkan sebagai bio.")


@Client.on_message(filters.me & filters.command(["setpfp"], cmd))
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.edit("**Foto Profil anda Berhasil Diubah.**")
    else:
        await message.edit(
            "`Balas ke foto apa pun untuk dipasang sebagai foto profile`"
        )
        await sleep(3)
        await message.delete()


@Client.on_message(filters.me & filters.command(["vpfp"], cmd))
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.edit("Foto profil tidak ditemukan!")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)


add_command_help(
    "profile",
    [
        ["block", "Untuk memblokir pengguna telegram"],
        ["unblock", "Untuk membuka pengguna yang anda blokir"],
        ["setname", "Untuk Mengganti Nama Telegram."],
        ["setbio", "Untuk Mengganti Bio Telegram."],
        [
            "setpfp",
            f"Balas Ke Gambar Ketik {cmd}setpfp Untuk Mengganti Foto Profil Telegram.",
        ],
        ["vpfp", "Untuk melihat foto profile pengguna saat ini."],
    ],
)
