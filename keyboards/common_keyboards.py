from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ButtonText:
    HELLO = "Hello!"
    WHATS_NEXT = "What's next!"
    BYE = "Bye!"


def get_on_start_kb() -> ReplyKeyboardMarkup:
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WHATS_NEXT)
    button_bye = KeyboardButton(text=ButtonText.BYE)
    first_row = [button_hello, button_help]
    second_row = [button_bye]
    markup = ReplyKeyboardMarkup(
        keyboard=[first_row, second_row],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return markup


def get_on_help_kb() -> ReplyKeyboardMarkup:
    numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "0️⃣"]
    buttons_row = [KeyboardButton(text=number) for number in numbers]
    # markup = ReplyKeyboardMarkup(
    #     keyboard=[buttons_row, buttons_row],
    #     resize_keyboard=True,
    # )
    # return markup

    builder = ReplyKeyboardBuilder()
    for num in numbers:
        builder.button(text=num)
    # builder.adjust(3, 3, 4)
    builder.adjust(3)
    builder.row(buttons_row[3], buttons_row[1])
    return builder.as_markup(resize_keyboard=False)


def get_actions_kb() -> ReplyKeyboardMarkup:
    # markup = ReplyKeyboardMarkup(
    #     keyboard=[]
    # )

    builder = ReplyKeyboardBuilder()
    builder.button(
        text="🌍 Send Location",
        request_location=True,
    )
    builder.button(
        text="☎️ Send My Phone",
        request_contact=True,
    )
    builder.button(
        text="📊 Send Poll",
        request_poll=KeyboardButtonPollType(),
    )
    builder.button(
        text="👾 Send Quiz",
        request_poll=KeyboardButtonPollType(type="quiz"),
    )
    builder.button(
        text="🍽️ Dinner?",
        request_poll=KeyboardButtonPollType(type="regular"),
    )
    builder.button(text=ButtonText.BYE)
    builder.adjust(1)
    return builder.as_markup(
        input_field_placeholder="Actions:",
        resize_keyboard=True,
    )
