import time
from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto
from aiogram.types import InputFile, InputMedia
from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice, PreCheckoutQuery
from aiogram.types.message import ContentType

token = '6346805628:AAH35_vQ61ziUyXC2PE5l_Pz1TbwQ90p5GE'

isExist = []

payment_token = '1661751239:TEST:JyTz-Q4ez-8p15-jMUL'

helloStart = "Вітаю✌️\n\nІнстаграм магазин maidenheaven.clo радий бачити вас🤝\n\nЦей телеграм бот створений задля комфортнішого вибору, перегляду та покупки товару вами😎"

questionWant = "Який саме тип речей вас цікавить?🧐"

searching = "Ось, що ми знайшли для вас🔍"

second = 'Секунду...⏱'

checker = 0

checker1 = 0

percentages = ["240", "50%", "100%"]

ikm = types.InlineKeyboardMarkup()

percentage_240 = types.InlineKeyboardButton(text='240 грн💸',callback_data='percentage_240')
percentage_50 = types.InlineKeyboardButton(text='50%🧐',callback_data='percentage_50')
percentage_100 = types.InlineKeyboardButton(text='😻100%😻',callback_data='percentage_100')

inline = types.InlineKeyboardButton(text="😍Через зв'язок з нами😍", callback_data="inline")

correctly = types.InlineKeyboardButton(text="Все вірно, відправити нам?✅", callback_data="correctly")

payment = types.InlineKeyboardButton(text="Заплатити✅", callback_data="payment")


item_Trousers = types.InlineKeyboardButton(text='Штани',callback_data='item_Trousers')
item_Sneakers = types.InlineKeyboardButton(text='Кросівки',callback_data='item_Sneakers')
item_snowySneakers = types.InlineKeyboardButton(text='Зимні кросівки',callback_data='item_snowySneakers')
item_womenJacket = types.InlineKeyboardButton(text='Жіноче пальто',callback_data='item_womenJacket')
item_Hat = types.InlineKeyboardButton(text='Шапка',callback_data='item_Hat')
item_Sweater = types.InlineKeyboardButton(text='Светр',callback_data='item_Sweater')
item_downJacket = types.InlineKeyboardButton(text='Пуховик',callback_data='item_downJacket')
item_Long = types.InlineKeyboardButton(text='Лонг',callback_data='item_Long')
item_hoody = types.InlineKeyboardButton(text='Худі',callback_data='item_hoody')
item_TShirt = types.InlineKeyboardButton(text='Футболка',callback_data='item_TShirt')
item_Suits = types.InlineKeyboardButton(text='Костюми',callback_data='item_Suits')
item_Bag = types.InlineKeyboardButton(text='Сумочка',callback_data='item_Bag')
item_Zip = types.InlineKeyboardButton(text='Зіпка',callback_data='item_Zip')
item_zipHoody = types.InlineKeyboardButton(text='Зіпка-Худі',callback_data='item_zipHoody')
item_Shorts = types.InlineKeyboardButton(text='Шорти',callback_data='item_Shorts')


allSupport = types.InlineKeyboardButton(text="🛠Тех.Підтримка🛠", callback_data="allsupport")

allOrder = types.InlineKeyboardButton(text="❤️Замовити❤️", callback_data="allorder")

chosenOrder = []
