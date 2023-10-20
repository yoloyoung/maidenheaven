from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

ziphoody_costFS = [2500]
ziphoody_costFS = ["Пухнаста кофта Struggle"]

ziphoody_cost = ["2500 грн"]
ziphoody_name = ["Пухнаста кофта Struggle"]

#1
ziphoodyCost = types.InlineKeyboardButton(text=f'{ziphoody_cost[0]}💸', callback_data="ziphoodyCost")
ziphoodyName = types.InlineKeyboardButton(text=f"{ziphoody_name[0]}😚", callback_data="ziphoodyName")


ziphoody = types.InlineKeyboardButton(text=ziphoody_name[0],callback_data='ziphoody')