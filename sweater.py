from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

sweater_costFS = [1500, 1600, 1500, 1600, 1500]
sweater_costFS = ["Светр Evangelion", "Светр Retro", "Светр Project", "Светр MCB", "Светр y2k"]

sweater_cost = ["1500 грн", "1500 грн", "1600 грн", "1500 грн", "1600 грн", "1500 грн"]
sweater_name = ["Светр Evangelion", "Светр Retro", "Светр Project", "Светр MCB", "Светр y2k"]

#1
EvangelionCost = types.InlineKeyboardButton(text=f'{sweater_cost[0]}💸', callback_data="EvangelionCost")
EvangelionName = types.InlineKeyboardButton(text=f"{sweater_name[0]}😚", callback_data="EvangelionName")
#2
RetroCost = types.InlineKeyboardButton(text=f'{sweater_cost[1]}💸', callback_data="RetroCost")
RetroName = types.InlineKeyboardButton(text=f"{sweater_name[1]}😚", callback_data="RetroName")
#3
ProjectCost = types.InlineKeyboardButton(text=f'{sweater_cost[2]}💸', callback_data="ProjectCost")
ProjectName = types.InlineKeyboardButton(text=f"{sweater_name[2]}😚", callback_data="ProjectName")
#4
MCBCost = types.InlineKeyboardButton(text=f'{sweater_cost[3]}💸', callback_data="MCBCost")
MCBName = types.InlineKeyboardButton(text=f"{sweater_name[3]}😚", callback_data="MCBName")
#5
y2kCost = types.InlineKeyboardButton(text=f'{sweater_cost[4]}💸', callback_data="y2kCost")
y2kName = types.InlineKeyboardButton(text=f"{sweater_name[4]}😚", callback_data="y2kName")

sweaterEvangelion = types.InlineKeyboardButton(text=sweater_name[0],callback_data='sweaterEvangelion')
sweaterRetro = types.InlineKeyboardButton(text=sweater_name[1],callback_data='sweaterRetro')
sweaterProject = types.InlineKeyboardButton(text=sweater_name[2],callback_data='sweaterProject')
sweaterMCB = types.InlineKeyboardButton(text=sweater_name[3],callback_data='sweaterMCB')
sweatery2k = types.InlineKeyboardButton(text=sweater_name[4],callback_data='sweatery2k')
