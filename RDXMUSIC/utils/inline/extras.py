from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="˹ᴍᴜsɪᴄ˼",
                    callback_data="help_callback"
                ),
                InlineKeyboardButton(
                    text="˹ᴍᴀɴᴀɢᴇᴍᴇɴᴛ˼",
                    callback_data="mbot_cb"),][
                InlineKeyboardButton(
                    text="˹sᴘᴇᴄɪᴀʟ ᴛᴀɢᴇʀ˼",
                    k_data="mplus HELP_TagAll"),
            ]
        ]
    )
    return upl


def cmds_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="˹ᴍᴜsɪᴄ˼",
                    callback_data="help_callback"
                ),
                InlineKeyboardButton(
                    text="˹ᴍᴀɴᴀɢᴇᴍᴇɴᴛ˼",
                    callback_data="mbot_cb"),][
                InlineKeyboardButton(
                    text="˹sᴘᴇᴄɪᴀʟ ᴛᴀɢᴇʀ˼",
                    k_data="mplus HELP_TagAll"),
            ]
        ]
    )
    return upl

