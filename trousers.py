from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

trousers_costFS = [1650, 1650, 1450, 1700, 1700, 1700, 1850, 1699, 1200, 1800]
trousers_brandFS = ["Реп штани Project", "Штани Doodle", "Штани Minus Two", "Штани Alien", "Штани JNCO", "Штани HCW", "Штани Feos", "Реп штани DDG", "Штани BlackWork", "Штани Keramo"]

trousers_cost = ["1650 грн", "1650 грн", "1450 грн", "1700 грн", "1700 грн", "1700 грн", "1850 грн", "1699 грн", "1200 грн", "1800 грн"]
trousers_brand = ["Реп штани Project", "Штани Doodle", "Штани Minus Two", "Штани Alien", "Штани JNCO", "Штани HCW", "Штани Feos", "Реп штани DDG", "Штани BlackWork", "Штани Keramo"]
 
#1
projectCost = types.InlineKeyboardButton(text=f'{trousers_cost[0]}💸', callback_data="projectcost")
projectName = types.InlineKeyboardButton(text=f"{trousers_brand[0]}😚", callback_data="projectname")
#2
doodleCost = types.InlineKeyboardButton(text=f'{trousers_cost[1]}💸', callback_data="doodlecost")
doodleName = types.InlineKeyboardButton(text=f"{trousers_brand[1]}😚", callback_data="doodlename")
#3
minusTwoCost = types.InlineKeyboardButton(text=f'{trousers_cost[2]}💸', callback_data="minustwocost")
minusTwoName = types.InlineKeyboardButton(text=f"{trousers_brand[2]}😚", callback_data="minustwoname")
#4
alienCost = types.InlineKeyboardButton(text=f'{trousers_cost[3]}💸', callback_data="aliencost")
alienName = types.InlineKeyboardButton(text=f"{trousers_brand[3]}😚", callback_data="alienname")
#5
jncoCost = types.InlineKeyboardButton(text=f'{trousers_cost[4]}💸', callback_data="jncocost")
jncoName = types.InlineKeyboardButton(text=f"{trousers_brand[4]}😚", callback_data="jnconame")
#6
hcwCost = types.InlineKeyboardButton(text=f'{trousers_cost[5]}💸', callback_data="hcwcost")
hcwName = types.InlineKeyboardButton(text=f"{trousers_brand[5]}😚", callback_data="hcwname")
#7
feosCost = types.InlineKeyboardButton(text=f'{trousers_cost[6]}💸', callback_data="feoscost")
feosName = types.InlineKeyboardButton(text=f"{trousers_brand[6]}😚", callback_data="feosname")
#8
ddgCost = types.InlineKeyboardButton(text=f'{trousers_cost[7]}💸', callback_data="ddgcost")
ddgName = types.InlineKeyboardButton(text=f"{trousers_brand[7]}😚", callback_data="ddgname")
#9
blackworkCost = types.InlineKeyboardButton(text=f'{trousers_cost[8]}💸', callback_data="blackworkcost")
blackworkName = types.InlineKeyboardButton(text=f"{trousers_brand[8]}😚", callback_data="blackworkname")
#10
keramoCost = types.InlineKeyboardButton(text=f'{trousers_cost[9]}💸', callback_data="keramocost")
keramoName = types.InlineKeyboardButton(text=f"{trousers_brand[9]}😚", callback_data="keramoname")

#Штаны
trousersProject = types.InlineKeyboardButton(text=trousers_brand[0],callback_data='trousersProject')
trousersDoodle = types.InlineKeyboardButton(text=trousers_brand[1],callback_data='trousersDoodle')
trousersMinusTwo = types.InlineKeyboardButton(text=trousers_brand[2],callback_data='trousersMinusTwo')
trousersAlien = types.InlineKeyboardButton(text=trousers_brand[3],callback_data='trousersAlien')
trousersJnco = types.InlineKeyboardButton(text=trousers_brand[4],callback_data='trousersJnco')
trousersHCW = types.InlineKeyboardButton(text=trousers_brand[5],callback_data='trousersHCW')
trousersFeos = types.InlineKeyboardButton(text=trousers_brand[6],callback_data='trousersFeos')
trousersDDG = types.InlineKeyboardButton(text=trousers_brand[7],callback_data='trousersDDG')
trousersBlackWork = types.InlineKeyboardButton(text=trousers_brand[8],callback_data='trousersBlackWork')
trousersKeramo = types.InlineKeyboardButton(text=trousers_brand[9],callback_data='trousersKeramo')