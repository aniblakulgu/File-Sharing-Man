# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL_2, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="📝 Bot Haqida", callback_data="help"),
                InlineKeyboardButton(text="🔒 Yopish", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Kanal 2", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="📝 Bot Haqida", callback_data="help"),
                InlineKeyboardButton(text="🔒 Yopish", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Kanal 1", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="Bot Haqida", callback_data="help"),
                InlineKeyboardButton(text="Yopish", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="📝 Bot Haqida", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="tytyty", url=client.invitelink),
                InlineKeyboardButton(text="brtu", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="Yopish", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="qowil", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="put3",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="qituvvv", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="bubuvv",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_CHANNEL_2:
        buttons = [
            [
                InlineKeyboardButton(text="Kanalga Qoshilish", url=client.invitelink),
                InlineKeyboardButton(text="Kanalga Qoshilish 2", url=client.invitelink2),
                InlineKeyboardButton(text="Kanalga Qoshilish 3", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="✅ QОSНILDIМ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
