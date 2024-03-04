from pyrogram.types import InlineKeyboardButton

import config
from RDXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="˹sᴜᴍᴍᴏɴ ᴍє˼", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="˹sᴜᴘᴘ๏ʀᴛ˼", url="https://t.me/+PtOLQT04ocMzOTJl"),
        ],
        [
            InlineKeyboardButton(
                text="˹ᴜᴘᴅᴀᴛᴇs˼",
                url="https://t.me/+m4oVCt2zFhYyMTdl"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            
            InlineKeyboardButton(text= "˹ʜєʟᴘ & ᴄᴍᴅ˼", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sᴜᴘᴘ๏ʀᴛ˼",
                url="https://t.me/+PtOLQT04ocMzOTJl"),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘ๏ʀᴛ˼", 
                url="https://t.me/+RObRa7kXPIJmMjU1"),],[
            InlineKeyboardButton(text="˹sᴜᴍᴍᴏɴ ᴍє ʙᴀʙʏ˼", url=f"https://t.me/{app.username}?startgroup=true",),],
        [
            InlineKeyboardButton(text="˹๏ᴡɴєʀ˼", user_id="1777270311"),
            InlineKeyboardButton(text="˹ᴜᴘᴅᴀᴛєѕ˼", url="https://t.me/+m4oVCt2zFhYyMTdl"),
        ],
    ]
    return buttons


def cmd_panel(_):
    buttons = [
        [
            
            InlineKeyboardButton(text= "˹ʜєʟᴘ & ᴄᴍᴅ˼", callback_data="CMDPANEL1"
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹sᴜᴘᴘ๏ʀᴛ˼",
                url="https://t.me/+PtOLQT04ocMzOTJl"),
            InlineKeyboardButton(
                text="˹sᴜᴘᴘ๏ʀᴛ˼", 
                url="https://t.me/+RObRa7kXPIJmMjU1"),],[
            InlineKeyboardButton(text="˹sᴜᴍᴍᴏɴ ᴍє ʙᴀʙʏ˼", url=f"https://t.me/{app.username}?startgroup=true",),],
        [
            InlineKeyboardButton(text="˹๏ᴡɴєʀ˼", user_id="1777270311"),
            InlineKeyboardButton(text="˹ᴜᴘᴅᴀᴛєѕ˼", url="https://t.me/+m4oVCt2zFhYyMTdl"),
        ],
    ]
    return buttons



