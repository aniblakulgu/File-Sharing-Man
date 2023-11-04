# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b>• Admin: <a href='https://t.me/KING_MODDER_UZ'>@KING_MODDER_UZ</b>
<b>• Kanal: <a href='https://t.me/UZGOANIME'>@UZGOANIME</b>

👨‍💻 <b>Savollar Boʻlsa: <a href='https://t.me/MAYKI_SOLO'>@MAYKI_SOLO</b>
"""

    close = [
        [InlineKeyboardButton("🔒 Yopish", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("📝 Bot Haqida", callback_data="help"),
            InlineKeyboardButton("🔒 Yopish", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("📝 Yordam", callback_data="about"),
            InlineKeyboardButton("🔒 Yopish", callback_data="close")
        ],
    ]

    ABOUT = """
 <b>❏ Botni ishlatish qo'llanmasi:
    1. Kanallarga obuna boling!
    2. Tekshirish Tugmasini bosing ✅
    3. Kanaldagi anime post past qismidagi yuklab olish tugmasini bosing</b>

👨‍💻 <b>Admin <a href='https://t.me/KING_MODDER_UZ'>@KING_MODDER_UZ</b>
"""
