from aiogram import executor
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from config import dp
from inline import menuStart, menuNft, Btn_right, Btn_left


@dp.message_handler(commands='start')
async def start(msg: Message):
    txt = f"Salom {msg.from_user.full_name}! Prince12 NFT Botga hush kelibsiz."
    await msg.answer_photo(open("picture/a1.jpg", "rb"), txt, reply_markup=menuStart)


@dp.callback_query_handler(text="nft_p")
async def nft(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a.jpg", "rb"), caption=f"Choose your lovely NFT pictures",
                                    reply_markup=menuNft)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="1")
async def one(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a2.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="2")
async def one2(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a3.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="3")
async def one3(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a4.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="5")
async def one4(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a5.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.callback_query_handler(text_contains="right")
async def right(call: CallbackQuery):
    # print("right")
    await call.message.answer_photo(open("picture/a.jpg", "rb"), reply_markup=Btn_right)
    # print("rightpic")
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains="left")
async def right(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a.jpg", "rb"), reply_markup=Btn_left)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="6")
async def one(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a6.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="7")
async def one2(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a7.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="8")
async def one3(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a8.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="9")
async def one4(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a9.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.callback_query_handler(text="10")
async def one4(call: CallbackQuery):
    await call.message.answer_photo(open("picture/a10.jpg.jpg", "rb"), caption=f"120 ETH🤑")
    await call.answer(cache_time=30)


@dp.message_handler(text="music")
async def music(msg: Message):
    await msg.answer(f"Musiqalar yaqin orada qo'shiladi, Nosozlik uchun uzr")


if __name__ == '__main__':
    executor.start_polling(dp)
