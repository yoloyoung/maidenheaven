from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

downJacket_costFS = [2500]
downJacket_costFS = ["Пуховик Hiraso"]

downJacket_cost = ["2500 грн"]
downJacket_name = ["Пуховик Hiraso"]

#1
downJacketCost = types.InlineKeyboardButton(text=f'{downJacket_cost[0]}💸', callback_data="downJacketCost")
downJacketName = types.InlineKeyboardButton(text=f"{downJacket_name[0]}😚", callback_data="downJacketName")

downJacket = types.InlineKeyboardButton(text=downJacket_name[0],callback_data="downJacket")