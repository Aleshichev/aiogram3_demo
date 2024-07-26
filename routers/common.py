import asyncio

from aiogram import F, types, Router
from aiogram.enums import ChatAction
from keyboards.common_keyboards import ButtonText
from aiogram.types import ReplyKeyboardRemove


router = Router(name=__name__)


@router.message(F.text == ButtonText.BYE)
async def handle_bye_message(message: types.Message):
    await message.answer(
        text="See you later! Click /start any time!",
        reply_markup=ReplyKeyboardRemove(),
    )


@router.message()
async def echo_message(message: types.Message):
    if message.poll:
        await message.forward(chat_id=message.chat.id)
        return

    await message.answer(text="Start processing")

    if message.sticker:
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.CHOOSE_STICKER,
        )
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Something new :)")
