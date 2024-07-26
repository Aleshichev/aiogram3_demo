from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from keyboards.inline_keyboards.info_kb import build_info_kb
from keyboards.common_keyboards import (
    get_on_start_kb,
    ButtonText,
    get_on_help_kb,
    get_actions_kb,
    )

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://ru.epicstars.com/wp-content/uploads/2017/05/telegram-bots-2.jpg"

    print("command text:", repr(message.text))
    await message.answer(
        text=f"{markdown.hide_link(url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
        reply_markup=get_on_start_kb(),
    )


@router.message(F.text == ButtonText.WHATS_NEXT)
@router.message(Command("help", prefix="!?/"))
async def handle_help(message: types.Message):

    text = markdown.text(
        markdown.markdown_decoration.quote("I'm an {echo} bot!"),
        markdown.text(
            "Send me",
            markdown.markdown_decoration.bold(
                markdown.text(markdown.underline("literally"), "any"),
            ),
            markdown.markdown_decoration.quote("message!"),
        ),
        sep="\n",
    )
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=get_on_help_kb(),
    )


@router.message(Command("more", prefix="!?/"))
async def handle_more(message: types.Message):
    markup=get_actions_kb()
    await message.answer(
        text="Choose action:",
        reply_markup=markup,
        )
    
    
@router.message(Command("info", prefix="!/"))
async def handle_info_command(message: types.Message):
    markup = build_info_kb()
    await message.answer(
        text="Resources and links:",
        reply_markup=markup,
    )
    