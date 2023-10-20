from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

zip_costFS = [1200, 1200, 1200]
zip_costFS = ["Зіп худі Dark Angel", "🔯Зіпка Vicinity🔯", "🦇Gothic Зіпка🦇"]

zip_cost = ["1200 грн", "1200 грн", "1200 грн"]
zip_name = ["Зіп худі Dark Angel", "🔯Зіпка Vicinity🔯", "🦇Gothic Зіпка🦇"]

#1
zipDKCost = types.InlineKeyboardButton(text=f'{zip_cost[0]}💸', callback_data="zipDKCost")
zipDKName = types.InlineKeyboardButton(text=f"{zip_name[0]}😚", callback_data="zipDKName")
#2
zipVicinityCost = types.InlineKeyboardButton(text=f'{zip_cost[1]}💸', callback_data="zipVicinityCost")
zipVicinityName = types.InlineKeyboardButton(text=f"{zip_name[1]}😚", callback_data="zipVicinityName")
#3
zipGothicCost = types.InlineKeyboardButton(text=f'{zip_cost[2]}💸', callback_data="zipGothicCost")
zipGothicName = types.InlineKeyboardButton(text=f"{zip_name[2]}😚", callback_data="zipGothicName")

zipDK = types.InlineKeyboardButton(text=zip_name[0],callback_data='zipDK')
zipVicinity = types.InlineKeyboardButton(text=zip_name[1],callback_data='zipVicinity')
zipGothic = types.InlineKeyboardButton(text=zip_name[2],callback_data='zipGothic')