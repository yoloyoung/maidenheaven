from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

costumes_costFS = [2400]
costumes_costFS = ["Костюми NAMED"]

costumes_cost = ["2400 грн"]
costumes_name = ["Костюми NAMED"]

#1
costumesCost = types.InlineKeyboardButton(text=f'{costumes_cost[0]}💸', callback_data="costumesCost")
costumesName = types.InlineKeyboardButton(text=f"{costumes_name[0]}😚", callback_data="costumesName")

costumes = types.InlineKeyboardButton(text=costumes_name[0],callback_data='costumes')