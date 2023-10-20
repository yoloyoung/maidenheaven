from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

womenCoat_costFS = [2100]
womenCoat_costFS = ["Зимове Пальто"]

womenCoat_cost = ["2100 грн"]
womenCoat_name = ["Зимове Пальто"]

#1
womenCoatCost = types.InlineKeyboardButton(text=f'{womenCoat_cost[0]}💸', callback_data="womenCoatCost")
womenCoatName = types.InlineKeyboardButton(text=f"{womenCoat_name[0]}😚", callback_data="womenCoatsName")

womenCoat = types.InlineKeyboardButton(text=womenCoat_name[0],callback_data='womenCoat')