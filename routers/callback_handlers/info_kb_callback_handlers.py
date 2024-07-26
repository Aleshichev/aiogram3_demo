from random import randint

from aiogram import Router, F
from keyboards.inline_keyboards.info_kb import (
        RandomNumCbData,
        RandomNumAction,
)
from aiogram.types import CallbackQuery

router = Router(name=__name__)


@router.callback_query(F.data == RandomNumAction.dice)
async def handle_random_num_dice(callback_query: CallbackQuery):
    await callback_query.answer(
        text=f"Your random dice: {randint(1, 21)}",
        cache_time=8,
    )


@router.callback_query(F.data == RandomNumAction.modal)
async def handle_random_num_modal_cb(callback_query: CallbackQuery):
    await callback_query.answer(
        text=f"Random num: {randint(1, 100)}", 
        cache_time=8,
        show_alert=True)
