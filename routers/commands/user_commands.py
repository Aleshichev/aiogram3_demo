import asyncio
import io
import csv
import aiohttp


from aiogram import types, Router
from aiogram.filters import Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode, ChatAction
from aiogram.utils.chat_action import ChatActionSender

from keyboards.inline_keyboards.actions_kb import build_actions_kb
from keyboards.inline_keyboards.shop_kb import build_shop_kb

router = Router(name=__name__)


@router.message(Command("code", prefix="!?/"))
async def handle_command_code(message: types.Message):
    text = markdown.text(
        "Here's Python code:",
        "",
        markdown.markdown_decoration.pre_language(
            markdown.text(
                "print('Hello world!')",
                "\n",
                "def foo():\n    return 'bar",
                sep="\n",
            ),
            language="python",
        ),
        sep="\n",
    )
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)


@router.message(Command("pic"))
async def handle_command_pic(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    url = "https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-superJumbo.jpg?quality=75&auto=webp"
    await message.reply_photo(
        photo=url,
    )


@router.message(Command("file"))
async def handle_command_file(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    file_path = "/home/igor/Pictures/cat.jpg"
    await message.reply_document(
        document=types.FSInputFile(
            path=file_path,
            filename="cat-big-photo.jpeg",
        ),
    )
    # message_sent.document.file_id


async def send_pic_file(message: types.Message):
    await asyncio.sleep(6)
    url = "https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-superJumbo.jpg?quality=75&auto=webp"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result_bytes = await response.read()
    await message.reply_document(
        document=types.BufferedInputFile(
            file=result_bytes,
            filename="cat-big-pic-cat.jpeg",
        ),
    )


@router.message(Command("pic_file"))
async def send_pic_file_buffered(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    action_sender = ChatActionSender(
        bot=message.bot,
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )

    async with action_sender:
        await send_pic_file(message)


@router.message(Command("text"))
async def send_txt_file(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    file = io.StringIO()
    file.write("Hello, World!\n")
    file.write("This is a text file.\n")
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="text.txt",
        ),
    )


@router.message(Command("csv"))
async def send_csv_file(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )
    file = io.StringIO()
    csv_writer = csv.writer(file)
    csv_writer.writerows(
        [
            ["Name", "Age", "City"],
            ["Igor", "21", "Kiev"],
            ["Ivan", "22", "Lviv"],
            ["Vasyl", "23", "Odessa"],
        ]
    )
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="people.csv",
        ),
    )


@router.message(Command("actions", prefix="!/"))
async def send_actions_message_w_kb(message: types.Message):
    await message.answer(
        text="Your actions:",
        reply_markup=build_actions_kb(),    
    )
    
    
@router.message(Command("shop", prefix="!?/"))
async def send_shop_message_kb(message: types.Message):
    await message.answer(
        text="Your shop actions:",
        reply_markup=build_shop_kb(),    
    )
