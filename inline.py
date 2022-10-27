from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menuStart = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="NFT Pictures", callback_data="nft_p"),
            InlineKeyboardButton(text="Musics", callback_data="music")
        ],
        [
            InlineKeyboardButton(text="Botni ulashish", switch_inline_query="Best of the Best Bot")
        ],
        [
            InlineKeyboardButton(text="Bizning Telegram Kanal", url="https://t.me/Alimardon_Boqijonov12")
        ]
    ]
)
menuNft = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3"),
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
        ],
        [
            InlineKeyboardButton(text="⏩", callback_data="right")
        ]
    ]
)
Btn_right = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="6", callback_data="6"),
            InlineKeyboardButton(text="7", callback_data="7"),
            InlineKeyboardButton(text="8", callback_data="8"),
            InlineKeyboardButton(text="9", callback_data="9"),
            InlineKeyboardButton(text="10", callback_data="10"),
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="left"),
            InlineKeyboardButton(text="⏩", callback_data="right")
        ]
    ]
)
Btn_left = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="1"),
            InlineKeyboardButton(text="2", callback_data="2"),
            InlineKeyboardButton(text="3", callback_data="3"),
            InlineKeyboardButton(text="4", callback_data="4"),
            InlineKeyboardButton(text="5", callback_data="5"),
        ],
        [
            InlineKeyboardButton(text="⏩", callback_data="right")
        ]
    ]
)
