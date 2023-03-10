# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Ported by @mrismanaziz
# FROM Man-Userbot
# Recode by @Gojo_satoru44

import asyncio
import random
import re

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import poci_cmd

usernexp = re.compile(r"@(\w{3,32})\[(.+?)\]")
nameexp = re.compile(r"\[([\w\S]+)\]\(tg://user\?id=(\d+)\)\[(.+?)\]")
emoji = "๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐คฃ ๐ญ ๐ ๐ ๐ ๐ ๐ฅฐ ๐ ๐คฉ ๐ฅณ ๐ค ๐ ๐ โบ๏ธ ๐ ๐ ๐ ๐ ๐คญ ๐ถ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐คช ๐ค ๐คจ ๐ง ๐ ๐ ๐ค ๐  ๐คฌ โน๏ธ ๐ ๐ ๐ ๐ฅบ ๐ณ ๐ฌ ๐ค ๐คซ ๐ฐ ๐จ ๐ง ๐ฆ ๐ฎ ๐ฏ ๐ฒ ๐ฑ ๐คฏ ๐ข ๐ฅ ๐ ๐ ๐ ๐ฃ ๐ฉ ๐ซ ๐คค ๐ฅฑ ๐ด ๐ช ๐ ๐ ๐ ๐ ๐ฒ ๐งฉ โ ๐ฏ ๐ณ ๐ญ๐ ๐ ๐ ๐ ๐ โค๏ธโ๐ฅ ๐ ๐ค ๐ค ๐ค โค๏ธ ๐งก ๐ ๐ ๐ ๐ ๐ ๐ ๐ต ๐ฆ ๐ฏ ๐ฑ ๐ถ ๐บ ๐ป ๐จ ๐ผ ๐น ๐ญ ๐ฐ ๐ฆ ๐ฆ ๐ฎ ๐ท ๐ฝ ๐ ๐ฆ ๐ฆ ๐ด ๐ธ ๐ฒ ๐ฆ ๐ ๐ฆ ๐ฆ ๐ข ๐ ๐ ๐ ๐ ๐ ๐ ๐ฉ ๐ ๐ฆฎ ๐โ๐ฆบ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฆ ๐ฆ ๐ฆฅ ๐ฆ ๐ ๐ฆ ๐ฆ ๐ฆ ๐ ๐ฆ ๐ฆง ๐ช ๐ซ ๐ฟ๏ธ ๐ฆจ ๐ฆก ๐ฆ ๐ฆฆ ๐ฆ ๐ ๐ ๐ฃ ๐ค ๐ฅ ๐ฆ ๐ฆ ๐ฆ ๐ฆ ๐๏ธ ๐ฆข ๐ฆฉ ๐ฆ ๐ฆ ๐ฆ ๐ง ๐ฆ ๐ฌ ๐ ๐ณ ๐ ๐  ๐ก ๐ฆ ๐ฆ ๐ฆ ๐ฆ ๐ ๐ฆช ๐ฆ ๐ท๏ธ ๐ฆ ๐ ๐ ๐ฆ ๐ฆ ๐ ๐ ๐ ๐ธ๏ธ ๐ ๐พ ๐ ๐คข ๐คฎ ๐คง ๐ค ๐ ๐ ๐ ๐ ๐ ๐ ๐ฅญ ๐ ๐ ๐ถ ๐ ๐ฅ ๐ ๐ ๐ ๐ ๐ ๐ฅ ๐  ๐ง ๐ฝ ๐ฅฆ ๐ฅ ๐ฅฌ ๐ฅ ๐ฅฏ ๐ฅ ๐ฅ ๐ ๐ฅ ๐ฐ ๐ฅ ๐ง ๐ ๐ง ๐ฅ ๐ฅ ๐ง ๐ฅ ๐ฅฉ ๐ ๐ ๐ฅ ๐ฏ ๐ฎ ๐ ๐ ๐ฅจ ๐ฅช ๐ญ ๐ ๐ง ๐ฅ ๐ ๐ฅซ ๐ฅฃ ๐ฅ ๐ฒ ๐ ๐ ๐ข ๐ฅ ๐ฑ ๐ ๐ฅก ๐ค ๐ฃ ๐ฆ ๐ฆช ๐ ๐ก ๐ฅ  ๐ฅฎ ๐ง ๐จ".split(
    " "
)


class FlagContainer:
    is_active = False


@bot.on(poci_cmd(outgoing=True, pattern=r"mention(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    query = event.pattern_match.group(1)
    mentions = f"@all {query}"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100500):
        mentions += f"[\u2063](tg://user?id={x.id} {query})"
    await bot.send_message(chat, mentions, reply_to=event.message.reply_to_msg_id)


@bot.on(poci_cmd(outgoing=True, pattern=r"emojitag(?: |$)(.*)"))
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True

        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()

        tags = list(
            map(
                lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})",
                await event.client.get_participants(chat),
            ),
        )
        current_pack = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            current_pack.append(participant)

            if len(current_pack) == 5:
                tags = list(
                    map(
                        lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})",
                        current_pack,
                    ),
                )
                current_pack = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(2)
    finally:
        FlagContainer.is_active = False


@bot.on(poci_cmd(outgoing=True, pattern=r"all(?: |$)(.*)"))
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True

        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()

        tags = list(
            map(
                lambda m: f"[{m.first_name}](tg://user?id={m.id})",
                await event.client.get_participants(chat),
            ),
        )
        jumlah = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            jumlah.append(participant)

            if len(jumlah) == 5:
                tags = list(
                    map(
                        lambda m: f"[{m.first_name}](tg://user?id={m.id})",
                        jumlah,
                    ),
                )
                jumlah = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(2)
    finally:
        FlagContainer.is_active = False


CMD_HELP.update(
    {
        "tag": f"**Plugin : **`tag`\
        \n\n  โข  **Syntax :** `{cmd}mention`\
        \n  โข  **Function : **Untuk Menmention semua anggota yang ada di group tanpa menyebut namanya.\
        \n\n  โข  **Syntax :** `{cmd}all` <text>\
        \n  โข  **Function : **Untuk Mengetag semua anggota Maksimal 3.000 orang yg akan ditag di grup untuk mengurangi flood wait telegram.\
        \n\n  โข  **Syntax :** `{cmd}emojitag` <text>\
        \n  โข  **Function : **Untuk Mengetag semua anggota di grup dengan random emoji berbeda.\
        \n\n  โข  **NOTE :** Untuk Memberhentikan Tag ketik `.restart`\
    "
    }
)
