from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

bag_costFS = [950, 1200, 850]
bag_costFS = ["Сумочка для дівчат💋", "👜Сумочка👜", "💼Сумочка на рибалку💼"]

bag_cost = ["950 грн", "1200 грн", "850 грн"]
bag_name = ["Сумочка для дівчат💋", "👜Сумочка👜", "💼Сумочка на рибалку💼"]

#1
bagFWCost = types.InlineKeyboardButton(text=f'{bag_cost[0]}💸', callback_data="bagFWCost")
bagFWName = types.InlineKeyboardButton(text=f"{bag_name[0]}😚", callback_data="bagFWName")
#2
bagCost = types.InlineKeyboardButton(text=f'{bag_cost[1]}💸', callback_data="bagCost")
bagName = types.InlineKeyboardButton(text=f"{bag_name[1]}😚", callback_data="bagName")
#3
bagFFCost = types.InlineKeyboardButton(text=f'{bag_cost[2]}💸', callback_data="bagFFCost")
bagFFName = types.InlineKeyboardButton(text=f"{bag_name[2]}😚", callback_data="bagFFName")

bag = types.InlineKeyboardButton(text=bag_name[0],callback_data='bag')
bagFW = types.InlineKeyboardButton(text=bag_name[1],callback_data='bagFW')
bagFF = types.InlineKeyboardButton(text=bag_name[2],callback_data='bagFF')