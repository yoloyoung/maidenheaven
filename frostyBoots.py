from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

frostyBoots_costFS = ["Зимні кросівки"]

frostyBoots_cost = ["2300 грн"]
frostyBoots_name = ["Зимні кросівки"]

#1
fronstyBootsCost = types.InlineKeyboardButton(text=f'{frostyBoots_cost[0]}💸', callback_data="fronstyBootsCost")
frostyBootsName = types.InlineKeyboardButton(text=f"{frostyBoots_name[0]}😚", callback_data="frostyBootsName")

frostyBoots = types.InlineKeyboardButton(text=frostyBoots_name[0],callback_data='frostyBoots')