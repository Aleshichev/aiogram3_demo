from aiogram import  types, F, Router

router = Router(name=__name__)


# @dp.message(lambda message: message.photo)  # True/False
# @dp.message(is_photo)                       # True/False
# @dp.message(F.photo, ~F.caption)  # True/False
# async def handle_message(message: types.Message):
#     await message.reply("Nice photo!")


@router.message(F.photo, ~F.caption)
async def handle_photo_wo_caption(message: types.Message):
    caption = "I can't see, sorry. Could you describe it please?"
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )


@router.message(F.photo, F.caption.contains("Nice"))  # True/False
async def handle_message(message: types.Message):
    await message.reply("What a pity!")


any_media_filter = F.photo | F.video | F.document


@router.message(any_media_filter, ~F.caption)
async def handle_any_media_wo_caption(message: types.Message):
    if message.document:
        await message.reply_document(
            document=message.document.file_id,
        )
    elif message.video:
        await message.reply_video(
            video=message.video.file_id,
        )
    else:
        await message.reply("I can't see")


@router.message(any_media_filter, F.caption)
async def handle_any_media_w_caption(message: types.Message):
    await message.reply(f"Smth is on media. Your text: {message.caption!r}")

