from config import *
from trousers import *
from sneakers import *
from initPics import *
from frostyBoots import *
from womenCoat import *
from hat import *
from sweater import *
from downJacket import *
from Long import *
from Hoody import *
from tShirt import *
from costumes import *
from bag import *
from zipp import *
from zipHoody import *
from shorts import *

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    try:
        #Обьявление глобальных переменных
        global beginQuestion
        global markupQuestion
        global checker
        #ЗавchosenOrder = []
        # chosenOrder.append(projectCost, projectName)
        # print(chosenOrder)ртывания в try: except:
        #Переменные
        cid = message.chat.id
        #Первое сообщение
        beginQuestion = await bot.send_message(cid, helloStart)
        #Товар
        #Добавление маркапов
        if checker == 0:
            ikm.add(item_Trousers, item_Sneakers, item_snowySneakers, item_womenJacket, item_Hat, item_Sweater, item_downJacket, item_Long, item_hoody, item_TShirt, item_Suits, item_Bag, item_Zip, item_zipHoody, item_Shorts)
            checker += 1
        markupQuestion = await bot.send_message(cid, questionWant,reply_markup=ikm,parse_mode='Markdown')
    except:
        await bot.send_message(cid, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')
        
    #Обработчик ошибок

@dp.callback_query_handler(lambda call: call.data == 'item_Trousers')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(trousersProject, trousersDoodle, trousersMinusTwo, trousersAlien, trousersJnco, trousersHCW, trousersFeos, trousersDDG, trousersBlackWork, trousersKeramo)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1.5)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_Sneakers')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(sneakersAdidas, sneakersSenj, sneakersRaalbckkBlack, sneakersRaalbckkWhite)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1.5)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_snowySneakers')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(frostyBoots)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1.5)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_womenJacket')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(womenCoat)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1.5)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_Sweater')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(sweaterEvangelion, sweaterRetro, sweaterProject, sweaterMCB, sweatery2k)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1.5)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_Hat')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(hat)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_hoody')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(hoodyMadeeExtreme, hoodyPistolKiss, hoodyCalifornia, hoodySkeletons, hoodyGhost, hoodyHoodie)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_downJacket')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(downJacket)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')


@dp.callback_query_handler(lambda call: call.data == 'item_Long')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(long)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_TShirt')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(tShirtsizeG, tShirtSize, tShirtExtreme, tShirtDestroyLonely, tShirtworldWide, tShirtLightning)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_Suits')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(costumes)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_Bag')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(bag, bagFW, bagFF)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_Zip')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(zipDK, zipGothic, zipVicinity)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.callback_query_handler(lambda call: call.data == 'item_zipHoody')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(ziphoody)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')


@dp.callback_query_handler(lambda call: call.data == 'item_Shorts')
async def searchTrousers(query: types.CallbackQuery):
    global user_id
    global forKeyboardMarkup
    try:
        buttonBack = KeyboardButton("Головне меню💫")
        Back = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonBack)
        #Переменные
        ist = types.InlineKeyboardMarkup()
        user_id = query.message.chat.id
        #Удаление предыдущих кнопок
        await beginQuestion.delete()
        await markupQuestion.delete()
        #Добавления маркапов
        ist.add(shortsproject, shortstrue, starsmth)
        forKeyboardMarkup = await bot.send_message(user_id, second, reply_markup = Back)
        time.sleep(1)
        #Добавления маркапов
        await bot.send_message(user_id, searching, reply_markup = ist,parse_mode='Markdown')
    #Обработчик ошибок
    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')





@dp.callback_query_handler()
async def clickProject(callback_query: types.CallbackQuery):
    global checker1
    global forEditing
    global msgforchosepred
    global chosenOrder
    global isExist
    call_data = callback_query.data
    user_id = callback_query.message.chat.id

    try:
        #1
        if call_data == "trousersProject":
            chosenOrder = []
            chosenOrder.append(trousers_cost[0])
            chosenOrder.append(trousers_brand[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(projectCost, projectName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            project = await bot.send_photo(user_id,photo=photoPathFproject, reply_markup=ifp, caption="Реп штани Project\nS/M/L/XL/2XL\nUNISEX\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(project)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
            

        #2
        elif call_data == "trousersDoodle":
            chosenOrder = []
            chosenOrder.append(trousers_cost[1])
            chosenOrder.append(trousers_brand[1])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(doodleCost, doodleName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            doodle = await bot.send_photo(user_id,photo=photoPathFdoodle, reply_markup=ifp, caption="Штани Doodle\nS/M/L/XL\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(doodle)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #3

        elif call_data == "trousersMinusTwo":
            chosenOrder = []
            chosenOrder.append(trousers_cost[2])
            chosenOrder.append(trousers_brand[2])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(minusTwoCost, minusTwoName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            minusTwo = await bot.send_photo(user_id,photo=photoPathFminustwo, reply_markup=ifp, caption="Штани Minus Two\nS/M/L/XL\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(minusTwo)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)         
        #4
        
        elif call_data == "trousersAlien":
            chosenOrder = []
            chosenOrder.append(trousers_cost[3])
            chosenOrder.append(trousers_brand[3])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(alienCost, alienName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            Alien = await bot.send_photo(user_id,photo=photoPathFalien, reply_markup=ifp, caption="Штани Alien\nS/M/L/XL\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(Alien)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
        #5   
        
        elif call_data == "trousersJnco":
            chosenOrder = []
            chosenOrder.append(trousers_cost[4])
            chosenOrder.append(trousers_brand[4])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(jncoCost, jncoName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            Jnco = await bot.send_photo(user_id,photo=photoPathFjnco, reply_markup=ifp, caption="Штани JNCO\nS/M/L/XL/2XL\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(Jnco)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
        #6    
        
        elif call_data == "trousersHCW":
            chosenOrder = []
            chosenOrder.append(trousers_cost[5])
            chosenOrder.append(trousers_brand[5])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(hcwCost, hcwName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            HCW = await bot.send_photo(user_id,photo=photoPathFhcw, reply_markup=ifp, caption="Штани Heaven can wait\nS/M/L/XL\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(HCW)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
        #7  
        
        elif call_data == "trousersFeos":
            chosenOrder = []
            chosenOrder.append(trousers_cost[6])
            chosenOrder.append(trousers_brand[6])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(feosCost, feosName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            Feos = await bot.send_photo(user_id,photo=photoPathFfeos, reply_markup=ifp, caption="Штани Feos\nS/M/L/XL\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(Feos)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
        #8  
        
        elif call_data == "trousersDDG":
            chosenOrder = []
            chosenOrder.append(trousers_cost[7])
            chosenOrder.append(trousers_brand[7])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(ddgCost, ddgName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            ddg = await bot.send_photo(user_id,photo=photoPathFddg, reply_markup=ifp, caption="Реп Штани DDG\nS/M/L/XL\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(ddg)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
        #9   
        
        elif call_data == "trousersBlackWork":
            chosenOrder = []
            chosenOrder.append(trousers_cost[8])
            chosenOrder.append(trousers_brand[8])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(blackworkCost, blackworkName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            blackwork = await bot.send_photo(user_id,photo=photoPathFblackwork, reply_markup=ifp, caption="Штани Blackwork\nS/M/L/XL/2XL\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(blackwork)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
        #10   
        
        elif call_data == "trousersKeramo":
            chosenOrder = []
            chosenOrder.append(trousers_cost[9])
            chosenOrder.append(trousers_brand[9])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(keramoCost, keramoName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            keramo = await bot.send_photo(user_id,photo=photoPathFkeramo, reply_markup=ifp, caption="Штани Keramo\nS/M/L/XL/2XL\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(keramo)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "sneakersAdidas":
            chosenOrder = []
            chosenOrder.append(sneakers_cost[0])
            chosenOrder.append(sneakers_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(adidasCost, adidasName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFadidas, reply_markup=ifp, caption="The South Park x adidas Campus 80s\n36-46\nЦіна залежить від розміру\nЦя пара доступна під замовлення\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
        

        if call_data == "sneakersSenj":
            chosenOrder = []
            chosenOrder.append(sneakers_cost[1])
            chosenOrder.append(sneakers_name[1])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(senjCost, senjName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFsenj, reply_markup=ifp, caption="Кросівки Senj\nРозміри 36-44\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)



        if call_data == "sneakersRaalbckkBlack":
            chosenOrder = []
            chosenOrder.append(sneakers_cost[2])
            chosenOrder.append(sneakers_name[2])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(raalbckkCostBlack, raalbckkNameBlack, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFraalbckkBlack, reply_markup=ifp, caption="Кросівки RAALBCKK\nРозміри 36-44\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
            


        if call_data == "sneakersRaalbckkWhite":
            chosenOrder = []
            chosenOrder.append(sneakers_cost[3])
            chosenOrder.append(sneakers_name[3])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(raalbckkCostWhite, raalbckkNameWhite, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFraalbckkWhite, reply_markup=ifp, caption="Кросівки RAALBCKK\nРозміри 36-44\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)


        
        if call_data == "sneakersNewRock":
            chosenOrder = []
            chosenOrder.append(sneakers_cost[4])
            chosenOrder.append(sneakers_name[4])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(newRockCost, newRockName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFNewRock, reply_markup=ifp, caption="Нью Роки\nРозміри 35-45(Менші розміри дешевші)\nЯкість матеріалу 10/10\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Кроссовки зимние

        if call_data == "frostyBoots":
            chosenOrder = []
            chosenOrder.append(frostyBoots_cost[0])
            chosenOrder.append(frostyBoots_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(fronstyBootsCost, frostyBootsName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFFrostyBoots, reply_markup=ifp, caption="Зимні кросівки\nРозміри: 35-46\nЯкість матеріалу 10/10\nДля зберігання тепла, всередині знаходиться хутро\nБагато різних кольорів у наявності🚨\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Пальтишко

        if call_data == "womenCoat":
            chosenOrder = []
            chosenOrder.append(frostyBoots_cost[0])
            chosenOrder.append(frostyBoots_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(womenCoatCost, womenCoatName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFwomenCoat, reply_markup=ifp, caption="⚡Жіноче Зимове Пальто⚡\nS/M/L/XL/XXL\nВироблено в Америці🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)


        #Шапка

        if call_data == "hat":
            chosenOrder = []
            chosenOrder.append(hat_cost[0])
            chosenOrder.append(hat_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(hatCost, hatName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFhat, reply_markup=ifp, caption="⚡Шапки Beanie⚡\n\nВироблено в Америці🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Свитера

        if call_data == "sweaterEvangelion":
            chosenOrder = []
            chosenOrder.append(sweater_cost[0])
            chosenOrder.append(sweater_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(EvangelionCost, EvangelionName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFEvangelion, reply_markup=ifp, caption="⚡Светр Evangelion⚡\n\nM/L/XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "sweaterRetro":
            chosenOrder = []
            chosenOrder.append(sweater_cost[1])
            chosenOrder.append(sweater_name[1])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(RetroCost, RetroName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFRetro, reply_markup=ifp, caption="⚡Светр Project⚡\n\nS/M/L/XL/2XLі🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "sweaterProject":
            chosenOrder = []
            chosenOrder.append(sweater_cost[2])
            chosenOrder.append(sweater_name[2])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(projectCost, projectName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFprojectS, reply_markup=ifp, caption="⚡Светр MCB⚡\n\nS/M/L/XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "sweaterMCB":
            chosenOrder = []
            chosenOrder.append(sweater_cost[3])
            chosenOrder.append(sweater_name[3])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(MCBCost, MCBName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFMCB, reply_markup=ifp, caption="⚡Светр y2k⚡\n\nM/L/XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "sweatery2k":
            chosenOrder = []
            chosenOrder.append(sweater_cost[4])
            chosenOrder.append(sweater_name[4])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(y2kCost, y2kName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFy2k, reply_markup=ifp, caption="⚡Шапки Beanie⚡\n\nВироблено в Америці🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Пуховик

        if call_data == "downJacket":
            chosenOrder = []
            chosenOrder.append(downJacket_cost[0])
            chosenOrder.append(downJacket_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(downJacketCost, downJacketName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFdownJacket, reply_markup=ifp, caption="⚡Пуховик Hiraso⚡\n\nS/M/L/XL/2XL/3XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)


        #Лонги

        if call_data == "long":
            chosenOrder = []
            chosenOrder.append(long_cost[0])
            chosenOrder.append(long_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(longCost, longName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFLong, reply_markup=ifp, caption="⚡Лонг moonscars⚡\n\n\M/L/XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Худи

        if call_data == "hoodyMadeeExtreme":
            chosenOrder = []
            chosenOrder.append(hoody_cost[0])
            chosenOrder.append(hoody_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(MadeeExtremeCost, MadeeExtremeName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFMadeeExtreme, reply_markup=ifp, caption="⚡Худі Madeextreme⚡\n\nM/L/XL/2XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "hoodyPistolKiss":
            chosenOrder = []
            chosenOrder.append(hoody_cost[1])
            chosenOrder.append(hoody_name[1])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(PistolKissCost, PistolKissName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFPistolKiss, reply_markup=ifp, caption="⚡Худі Pistol Kiss⚡\n\n\S/M/L/XL/2XL/3XL/4XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "hoodyCalifornia":
            chosenOrder = []
            chosenOrder.append(hoody_cost[2])
            chosenOrder.append(hoody_name[2])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(CaliforniaCost, CaliforniaName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFCalifornia, reply_markup=ifp, caption="⚡Пухнаста худі California⚡\n\nS/M/L/XL/2XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "hoodySkeletons":
            chosenOrder = []
            chosenOrder.append(hoody_cost[3])
            chosenOrder.append(hoody_name[3])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(SkeletonsCost, SkeletonsName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFSkeletons, reply_markup=ifp, caption="⚡Худі skeletons in flame⚡\n\nM/L/XL/2XL🦅\nUNISEX💋\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "hoodyGhost":
            chosenOrder = []
            chosenOrder.append(hoody_cost[4])
            chosenOrder.append(hoody_name[4])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(GhostCost, GhostName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFGhost, reply_markup=ifp, caption="⚡Худі kids see ghosts⚡\n\nS/M/L/XL🦅\nUNISEX💋\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "hoodyHoodie":
            chosenOrder = []
            chosenOrder.append(hoody_cost[5])
            chosenOrder.append(hoody_name[5])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(HoodieCost, HoodieName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFHoodie, reply_markup=ifp, caption="⚡Hoodie⚡\n\nM/L/XL/XXL🦅\nUNISEX👄\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)


        #Футболки


        if call_data == "tShirtsizeG":
            chosenOrder = []
            chosenOrder.append(tShirt_cost[0])
            chosenOrder.append(tShirt_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(overSizeGCost, overSizeGName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFsizeG, reply_markup=ifp, caption="⚡Футболка Oversize GPunk⚡\n\nM/L/XL/2XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "tShirtSize":
            chosenOrder = []
            chosenOrder.append(tShirt_cost[1])
            chosenOrder.append(tShirt_name[1])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(overSizeCost, overSizeName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFsize, reply_markup=ifp, caption="⚡Оверсайз футболка⚡\n\nS/M/L/XL/2XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "tShirtExtreme":
            chosenOrder = []
            chosenOrder.append(tShirt_cost[2])
            chosenOrder.append(tShirt_name[2])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(madeExtremeCost, madeExtremeName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFextreme, reply_markup=ifp, caption="⚡Футболка Made extreme⚡\n\nM/L/XL/2XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "tShirtDestroyLonely":
            chosenOrder = []
            chosenOrder.append(tShirt_cost[3])
            chosenOrder.append(tShirt_name[3])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(destroyLonelyCost, destroyLonelyName, allSupport, allOrder)
            if checker1 == 1:
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFdestroyLonely, reply_markup=ifp, caption="⚡Футболка Destroylonely⚡\n\nM/L/XL/2XL/3XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "tShirtworldWide":
            chosenOrder = []
            chosenOrder.append(tShirt_cost[4])
            chosenOrder.append(tShirt_name[4])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(worldWideCost, worldWideName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFworldWide, reply_markup=ifp, caption="⚡Футболка worldwide⚡\n\nS/M/L/XL/2XL/3XL/4XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "tShirtLightning":
            chosenOrder = []
            chosenOrder.append(tShirt_cost[5])
            chosenOrder.append(tShirt_name[5])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(LightningCost, LightningName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFlightning, reply_markup=ifp, caption="⚡Футболочка Lightning⚡\n\nS/M/L/XL/2XL🦅\nUNISEX👄\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Костюмы

        if call_data == "costumes":
            chosenOrder = []
            chosenOrder.append(costumes_cost[0])
            chosenOrder.append(costumes_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(costumesCost, costumesName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFcostumes, reply_markup=ifp, caption="⚡Костюми NAMED⚡\n\nS/M/L/XL🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        
        #Сумки

        
        if call_data == "bagFW":
            chosenOrder = []
            chosenOrder.append(bag_cost[0])
            chosenOrder.append(bag_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(bagFWCost, bagFWName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFW, reply_markup=ifp, caption="⚡Сумочка для дівчат💋⚡\n\n23.5 х 7.5 х 14см🦅\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
        
        if call_data == "bag":
            chosenOrder = []
            chosenOrder.append(bag_cost[1])
            chosenOrder.append(bag_name[1])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(bagCost, bagName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFbag, reply_markup=ifp, caption="⚡👜Сумочка👜⚡\n\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        
        if call_data == "bagFF":
            chosenOrder = []
            chosenOrder.append(bag_cost[2])
            chosenOrder.append(bag_name[2])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(bagFFCost, bagFFName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFFF, reply_markup=ifp, caption="⚡💼Сумочка на рибалку💼⚡\n\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Зипка

        if call_data == "zipDK":
            chosenOrder = []
            chosenOrder.append(zip_cost[0])
            chosenOrder.append(zip_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(zipDKCost, zipDKName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFdarkAngel, reply_markup=ifp, caption="⚡Зіп худі Dark Angel⚡\nS/M/L/XL/2XL\nUNISEX💋\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)
            
        if call_data == "zipVicinity":
            chosenOrder = []
            chosenOrder.append(zip_cost[1])
            chosenOrder.append(zip_name[1])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(zipVicinityCost, zipVicinityName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFvicinity, reply_markup=ifp, caption="⚡🔯Зіпка Vicinity🔯⚡\nS/M/L/XL/2XL\nUNISEX💋\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "zipGothic":
            chosenOrder = []
            chosenOrder.append(zip_cost[2])
            chosenOrder.append(zip_name[2])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(zipGothicCost, zipGothicName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFgothic, reply_markup=ifp, caption="⚡🦇Gothic Зіпка🦇⚡\nM/L/XL/2XL\nUNISEX💋\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Зипка-Худак

        
        if call_data == "ziphoody":
            chosenOrder = []
            chosenOrder.append(ziphoody_cost[0])
            chosenOrder.append(ziphoody_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(ziphoodyCost, ziphoodyName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFzipHoody, reply_markup=ifp, caption="⚡Пухнаста кофта Struggle⚡\nS/M/L/XL/2XL\n\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        #Шорты

        if call_data == "shortsproject":
            chosenOrder = []
            chosenOrder.append(shorts_cost[0])
            chosenOrder.append(shorts_name[0])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(projectCost, projectName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFshortsProject, reply_markup=ifp, caption="⚡Шорти Project⚡\nS/M/L/XL/2XL\n\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "shortstrue":
            chosenOrder = []
            chosenOrder.append(shorts_cost[1])
            chosenOrder.append(shorts_name[1])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(trueCost, trueName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFshortsTrue, reply_markup=ifp, caption="⚡Шорти для тру реперів⚡\nS/M/L/XL/2XL\n\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)

        if call_data == "starsmth":
            chosenOrder = []
            chosenOrder.append(shorts_cost[2])
            chosenOrder.append(shorts_name[2])
            print(chosenOrder)
            ifp = types.InlineKeyboardMarkup()
            ifp.add(starCost, starName, allSupport, allOrder)
            if checker1 == 1: 
                await forEditing.delete()
                checker1 += 1
            adidas = await bot.send_photo(user_id,photo=photoPathFshortsStar, reply_markup=ifp, caption="⚡Шорти Star Pattern⚡\nS/M/L/XL/2XL\n\nЯкість матеріалу 10/10🕶️\nДоставка 11-22 робочих днів🚚")
            if len(isExist) == 0 or len(isExist) == 1:
                isExist.append(adidas)
                print(len(isExist))
            if len(isExist) == 2:
                await isExist[0].delete()
                isExist.pop(0)






        

            



            













        if call_data == "allorder":
            ifo = types.InlineKeyboardMarkup()
            ifo.add(percentage_240,percentage_50,percentage_100)
            TEXTinfo = await bot.send_message(user_id, text="Якщо вибраний варіант, не є предоплатою 100% від ціни товару, тоді ви доплатите іншу кількість грошей з комісією на Новій Почті✉️")
            TEXTchoose = await bot.send_message(user_id, text="Бажаєте замовити предоплатою💗", reply_markup=ifo)

        if call_data == "allsupport":
            await bot.send_message(user_id, text="Надішліть нам будь ласка відомості про проблему в нашому боті😇")
            await bot.send_message(user_id, text="Дякую, що допомагаєте покращувати роботу телеграму боту💗")
            await bot.send_message(user_id, text="📎Наш телеграм айді: @MHshopUkraine📎")

        if call_data == "percentage_240":
            chosenOrder.append(percentages[0])
            ifpm = types.InlineKeyboardMarkup()
            ifpm.add(inline)
            TEXTpayment_240 = await bot.send_message(user_id, text="Ви обрали предоплату 240 гривень✅")
            TEXTsendTY = await bot.send_message(user_id, text="Як бажаєте відправити гроші на наші реквізити?", reply_markup=ifpm)
        elif call_data == "percentage_50":
            chosenOrder.append(percentages[1])
            ifpm = types.InlineKeyboardMarkup()
            ifpm.add(inline)
            TEXTpayment_50 = await bot.send_message(user_id, text="Ви обрали предоплату 50% від ціни товару✅")
            TEXTsendTY = await bot.send_message(user_id, text="Як бажаєте відправити гроші на наші реквізити?", reply_markup=ifpm)
        elif call_data == "percentage_100":
            chosenOrder.append(percentages[2])
            ifpm = types.InlineKeyboardMarkup()
            ifpm.add(inline)
            TEXTpayment_100 = await bot.send_message(user_id, text="Ви обрали предоплату 100% від ціни товару✅")
            TEXTsendTY = await bot.send_message(user_id, text="Як бажаєте відправити гроші на наші реквізити?", reply_markup=ifpm)

        if call_data == "inline":
            global purchase
            ifcc = InlineKeyboardMarkup()
            ifcc.add(correctly)
            purchase = await bot.send_message(user_id, text=f"💌Ім'я речі: {chosenOrder[1]}💌\n\n💸Ціна: {chosenOrder[0]} гривень💸\n\n💳Предоплата: {chosenOrder[2]}💳\n\n🌼Айді замовника: {user_id}🌼\n\n👀Нікнейм замовника: {callback_query.from_user.username}👀")
            await bot.send_message(user_id, text="Замовлення, що ви зробили, вірне?", reply_markup=ifcc)

        if call_data == "correctly":
            await bot.send_message(6471709977, text=f"👀Нове замовлення👀 \n\n{purchase}")
            await bot.send_message(user_id, text="Замовлення успішно відправлено нам✅")
            await bot.send_message(user_id, text="Найближчим часом з вами зв'яжеться наш менеджер задля уточненння деталей замовлення😇")

    except Exception as ex:
        await bot.send_message(user_id, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

@dp.message_handler()
async def support(message: types.Message):
    global beginQuestion
    global markupQuestion
    global ikm
    try:
        if message.text == "Головне меню💫":
            cid = message.chat.id
            ikm = types.InlineKeyboardMarkup()
            ikm.add(item_Trousers, item_Sneakers, item_snowySneakers, item_womenJacket, item_Hat, item_Sweater, item_downJacket, item_Long, item_hoody, item_TShirt, item_Suits, item_Bag, item_Zip, item_zipHoody, item_Shorts)
            beginQuestion = await bot.send_message(cid, helloStart)
            markupQuestion = await bot.send_message(cid, questionWant,reply_markup=ikm,parse_mode='Markdown')
    except Exception as ex:
        await bot.send_message(cid, text="Помилка, задля її усунення, пропишіть команду /start👀", parse_mode='Markdown')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)