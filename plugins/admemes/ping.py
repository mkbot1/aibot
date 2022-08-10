"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂" 
REPO = "<b>നോക്കി നിന്നോ ഇപ്പൊ കിട്ടും </b>"
CHANNEL = "<b>𝗖𝗛𝗔𝗡𝗡𝗘𝗟</b> ›› url='https://t.me/MkTgBots'\n\n<b>𝙈𝙊𝙑𝙄𝙀 𝙂𝙍𝙊𝙐𝙋 ›› https://t.me/AnyMoviezRequest</b>\n\n<b>𝙈𝙐𝙎𝙄𝘾 𝙂𝙍𝙊𝙐𝙋 ›› https://t.me/AnySongsRequest</b>"
AJAX = "<b>Link ›› url='https://bit.ly/3oWHMBw'</b>"
YTPLINK = "<b>Link ›› url='https://bit.ly/3oWHMBw'</b>"
GPLINK = "CED2SXCZ1HLEKJE1"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("faisal", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(AJAX)
    
    
@Client.on_message(filters.command("gpay", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(GPLINK)

    
@Client.on_message(filters.command("youtubepremium", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(YTPLINK)

