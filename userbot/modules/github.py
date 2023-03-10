# Copyright (C) 2021 Catuserbot <https://github.com/sandy1709/catuserbot>
# FROM Man-Userbot
# Recode by @Gojo_satoru44

import os

import aiohttp
import requests
from pySmartDL import SmartDL

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_delete, edit_or_reply, poci_cmd, reply_id

ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")


@poci_cmd(pattern="github( -l(\d+))? ([\s\S]*)")
async def _(event):
    "Get info about an GitHub User"
    reply_to = await reply_id(event)
    username = event.pattern_match.group(3)
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session, session.get(URL) as request:
        if request.status == 404:
            return await edit_delete(event, "`" + username + " Not Found`")
        catevent = await edit_or_reply(event, "`fetching github info ...`")
        result = await request.json()
        photo = result["avatar_url"]
        if result["bio"]:
            result["bio"] = result["bio"].strip()
        repos = []
        sec_res = requests.get(result["repos_url"])
        if sec_res.status_code == 200:
            limit = event.pattern_match.group(2)
            limit = 5 if not limit else int(limit)
            for repo in sec_res.json():
                repos.append(f"[{repo['name']}]({repo['html_url']})")
                limit -= 1
                if limit == 0:
                    break
        REPLY = "**GitHub Info for** `{username}`\
                \nš¤ **Name :** [{name}]({html_url})\
                \nš§ **Type :** `{type}`\
                \nš¢ **Company :** `{company}`\
                \nš­ **Blog :** {blog}\
                \nš **Location :** `{location}`\
                \nš **Bio :** __{bio}__\
                \nā¤ļø **Followers :** `{followers}`\
                \nš **Following :** `{following}`\
                \nš **Public Repos :** `{public_repos}`\
                \nš **Public Gists :** `{public_gists}`\
                \nš **Profile Created :** `{created_at}`\
                \nāļø **Profile Updated :** `{updated_at}`".format(
            username=username, **result
        )

        if repos:
            REPLY += "\nš **Some Repos** : " + " | ".join(repos)
        downloader = SmartDL(photo, ppath, progress_bar=False)
        downloader.start(blocking=False)
        await event.client.send_file(
            event.chat_id,
            ppath,
            caption=REPLY,
            reply_to=reply_to,
        )
        os.remove(ppath)
        await catevent.delete()


CMD_HELP.update(
    {
        "github": f"**Plugin : **`github`\
        \n\n  ā¢  **Syntax :** `{cmd}github` <username>\
        \n  ā¢  **Function : **Menampilkan informasi tentang user di GitHub dari username yang diberikan\
    "
    }
)
