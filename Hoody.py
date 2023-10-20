from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

hoody_costFS = [1750, 1300, 1400, 950, 1200, 1000]
hoody_nameFS = ["Худі Madeextreme", "Худі Pistol Kiss", "Пухнаста худі California", "Худі skeletons in flame", "Худі kids see ghosts", "Hoodie"]

hoody_cost = ["1750 грн", "1300 грн", "1400 грн", "950 грн", "1200 грн", "1000 грн"]
hoody_name = ["Худі Madeextreme", "Худі Pistol Kiss", "Пухнаста худі California", "Худі skeletons in flame", "Худі kids see ghosts", "Hoodie"]

#1
MadeeExtremeCost = types.InlineKeyboardButton(text=f'{hoody_cost[0]}💸', callback_data="MadeeExtremeCost")
MadeeExtremeName = types.InlineKeyboardButton(text=f"{hoody_name[0]}😚", callback_data="MadeeExtremeName")
#2
PistolKissCost = types.InlineKeyboardButton(text=f'{hoody_cost[1]}💸', callback_data="PistolKissCost")
PistolKissName = types.InlineKeyboardButton(text=f"{hoody_name[1]}😚", callback_data="PistolKissName")
#3
CaliforniaCost = types.InlineKeyboardButton(text=f'{hoody_cost[2]}💸', callback_data="CaliforniaCost")
CaliforniaName = types.InlineKeyboardButton(text=f"{hoody_name[2]}😚", callback_data="CaliforniaName")
#4
SkeletonsCost = types.InlineKeyboardButton(text=f'{hoody_cost[3]}💸', callback_data="SkeletonsCost")
SkeletonsName = types.InlineKeyboardButton(text=f"{hoody_name[3]}😚", callback_data="SkeletonsName")
#5
GhostCost = types.InlineKeyboardButton(text=f'{hoody_cost[4]}💸', callback_data="GhostCost")
GhostName = types.InlineKeyboardButton(text=f"{hoody_name[4]}😚", callback_data="GhostName")
#6
HoodieCost = types.InlineKeyboardButton(text=f'{hoody_cost[5]}💸', callback_data="HoodieCost")
HoodieName = types.InlineKeyboardButton(text=f"{hoody_name[5]}😚", callback_data="HoodieName")

hoodyMadeeExtreme = types.InlineKeyboardButton(text=hoody_name[0],callback_data='hoodyMadeeExtreme')
hoodyPistolKiss = types.InlineKeyboardButton(text=hoody_name[1],callback_data='hoodyPistolKiss')
hoodyCalifornia = types.InlineKeyboardButton(text=hoody_name[2],callback_data='hoodyCalifornia')
hoodySkeletons = types.InlineKeyboardButton(text=hoody_name[3],callback_data='hoodySkeletons')
hoodyGhost = types.InlineKeyboardButton(text=hoody_name[4],callback_data='hoodyGhost')
hoodyHoodie = types.InlineKeyboardButton(text=hoody_name[5],callback_data='hoodyHoodie')
