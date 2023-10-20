from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

shorts_costFS = [1100, 1200, 1350, 2200, 3000]
shorts_costFS = ["Шорти Project", "🔫Шорти для тру реперів🔫", "✨Шорти Star Pattern✨"]

shorts_cost = ["1100 грн", "1200 грн", "1350 грн", "2200 грн", "3000 грн"]
shorts_name = ["Шорти Project", "🔫Шорти для тру реперів🔫", "✨Шорти Star Pattern✨"]



#1
projectCost = types.InlineKeyboardButton(text=f'{shorts_cost[0]}💸', callback_data="projectCost")
projectName = types.InlineKeyboardButton(text=f"{shorts_name[0]}😚", callback_data="projectName")
#2
trueCost = types.InlineKeyboardButton(text=f'{shorts_cost[1]}💸', callback_data="senCost")
trueName = types.InlineKeyboardButton(text=f"{shorts_name[1]}😚", callback_data="trueName")
#3
starCost = types.InlineKeyboardButton(text=f'{shorts_cost[2]}💸', callback_data="starCost")
starName = types.InlineKeyboardButton(text=f"{shorts_name[2]}😚", callback_data="starName")

shortsproject = types.InlineKeyboardButton(text=shorts_name[0],callback_data='shortsproject')
shortstrue = types.InlineKeyboardButton(text=shorts_name[1],callback_data='shortstrue')
starsmth = types.InlineKeyboardButton(text=shorts_name[2],callback_data='starsmth')