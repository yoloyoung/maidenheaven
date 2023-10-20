from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

hat_costFS = [800]
hat_costFS = ["Шапки Beanie"]

hat_cost = ["800 грн"]
hat_name = ["Шапки Beanie"]

#1
hatCost = types.InlineKeyboardButton(text=f'{hat_cost[0]}💸', callback_data="hatCost")
hatName = types.InlineKeyboardButton(text=f"{hat_name[0]}😚", callback_data="hatName")

hat = types.InlineKeyboardButton(text=hat_name[0],callback_data='hat')