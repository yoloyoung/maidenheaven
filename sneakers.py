from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

sneakers_costFS = [7000, 2600, 2600, 2200, 3000]
sneakers_costFS = ["Adidas Campus", "Кросівки Senj", "Кросівки RAALBCKK", "Кросівки RAALBCKK", "Кросівки Нью Роки"]

sneakers_cost = ["7000 грн", "2600 грн", "2600 грн", "2200 грн", "3000 грн"]
sneakers_name = ["Adidas Campus", "Кросівки Senj", "Кросівки RAALBCKK", "Кросівки RAALBCKK", "Кросівки Нью Роки"]



#1
adidasCost = types.InlineKeyboardButton(text=f'{sneakers_cost[0]}💸', callback_data="adidasCost")
adidasName = types.InlineKeyboardButton(text=f"{sneakers_name[0]}😚", callback_data="adidasName")
#2
senjCost = types.InlineKeyboardButton(text=f'{sneakers_cost[1]}💸', callback_data="senCost")
senjName = types.InlineKeyboardButton(text=f"{sneakers_name[1]}😚", callback_data="senjName")
#3
raalbckkCostBlack = types.InlineKeyboardButton(text=f'{sneakers_cost[2]}💸', callback_data="raalbckkCostBlack")
raalbckkNameBlack = types.InlineKeyboardButton(text=f"{sneakers_name[2]}😚", callback_data="raalbckkNameBlack")
#4
raalbckkCostWhite = types.InlineKeyboardButton(text=f'{sneakers_cost[3]}💸', callback_data="raalbckkCostWhite")
raalbckkNameWhite = types.InlineKeyboardButton(text=f"{sneakers_name[3]}😚", callback_data="raalbckkNameWhite")
#5
newRockCost = types.InlineKeyboardButton(text=f'{sneakers_cost[4]}💸', callback_data="raalbckkCostWhite")
newRockName = types.InlineKeyboardButton(text=f"{sneakers_name[4]}😚", callback_data="raalbckkNameWhite")


sneakersAdidas = types.InlineKeyboardButton(text=sneakers_name[0],callback_data='sneakersAdidas')
sneakersSenj = types.InlineKeyboardButton(text=sneakers_name[1],callback_data='sneakersSenj')
sneakersRaalbckkBlack = types.InlineKeyboardButton(text=sneakers_name[2],callback_data='sneakersRaalbckkBlack')
sneakersRaalbckkWhite = types.InlineKeyboardButton(text=sneakers_name[3],callback_data='sneakersRaalbckkWhite')
sneakersNewRock = types.InlineKeyboardButton(text=sneakers_name[4],callback_data='sneakersNewRock')