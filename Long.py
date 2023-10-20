from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

long_costFS = [1000]
long_costFS = ["Лонг moonscars"]

long_cost = ["1000 грн"]
long_name = ["Лонг moonscars"]

#1
longCost = types.InlineKeyboardButton(text=f'{long_cost[0]}💸', callback_data="longCost")
longName = types.InlineKeyboardButton(text=f"{long_name[0]}😚", callback_data="longName")

long = types.InlineKeyboardButton(text=long_name[0],callback_data='long')