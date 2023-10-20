from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto

tShirt_costFS = [1000, 850, 1100, 900, 750, 950]
tShirt_costFS = ["Футболка Oversize GPunk", "Оверсайз футболка", "Футболка Made extreme", "Футболка Destroylonely", "Футболка worldwide", "Футболочка Lightning"]

tShirt_cost = ["1000 грн", "850 грн", "1100 грн", "900 грн", "750 грн", "950 грн"]
tShirt_name = ["Футболка Oversize GPunk", "Оверсайз футболка", "Футболка Made extreme", "Футболка Destroylonely", "Футболка worldwide", "Футболочка Lightning"]



#1
overSizeGCost = types.InlineKeyboardButton(text=f'{tShirt_cost[0]}💸', callback_data="overSizeGCost")
overSizeGName = types.InlineKeyboardButton(text=f"{tShirt_name[0]}😚", callback_data="overSizeGName")
#2
overSizeCost = types.InlineKeyboardButton(text=f'{tShirt_cost[1]}💸', callback_data="overSizeCost")
overSizeName = types.InlineKeyboardButton(text=f"{tShirt_name[1]}😚", callback_data="overSizeName")
#3
madeExtremeCost = types.InlineKeyboardButton(text=f'{tShirt_cost[2]}💸', callback_data="madeExtremeCost")
madeExtremeName = types.InlineKeyboardButton(text=f"{tShirt_name[2]}😚", callback_data="madeExtremeName")
#4
destroyLonelyCost = types.InlineKeyboardButton(text=f'{tShirt_cost[3]}💸', callback_data="destroyLonelyCost")
destroyLonelyName = types.InlineKeyboardButton(text=f"{tShirt_name[3]}😚", callback_data="destroyLonelyName")
#5
worldWideCost = types.InlineKeyboardButton(text=f'{tShirt_cost[4]}💸', callback_data="worldWideCost")
worldWideName = types.InlineKeyboardButton(text=f"{tShirt_name[4]}😚", callback_data="worldWideName")
#6
LightningCost = types.InlineKeyboardButton(text=f'{tShirt_cost[5]}💸', callback_data="LightningCost")
LightningName = types.InlineKeyboardButton(text=f"{tShirt_name[5]}😚", callback_data="LightningName")


tShirtsizeG = types.InlineKeyboardButton(text=tShirt_name[0],callback_data='tShirtsizeG')
tShirtSize = types.InlineKeyboardButton(text=tShirt_name[1],callback_data='tShirtSize')
tShirtExtreme = types.InlineKeyboardButton(text=tShirt_name[2],callback_data='tShirtExtreme')
tShirtDestroyLonely = types.InlineKeyboardButton(text=tShirt_name[3],callback_data='tShirtDestroyLonely')
tShirtworldWide = types.InlineKeyboardButton(text=tShirt_name[4],callback_data='tShirtworldWide')
tShirtLightning = types.InlineKeyboardButton(text=tShirt_name[5],callback_data='tShirtLightning')