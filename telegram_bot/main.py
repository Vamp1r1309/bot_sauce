from aiogram import types, executor, Dispatcher, Bot


TOKEN = "Ваш TOKEN"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

import func
import markups as nav
import db


@dp.message_handler(commands=['start'])
async def go_bot(message: types.Message):
    await bot.send_message(message.chat.id, 'Закупка', reply_markup=nav.mainMenu)


# --------------------------------------------------------------------------------------- Воронеж --------------------------------------------------------------------------------------------------------
@dp.message_handler(text=[str(i) for i in range(1800, 10000)])
async def get_Voronezj(message: types.Message):
    from math import ceil

    try:
        await message.answer(f"Сметана - {round(int(message.text) * 0.13 / 2.2), 3} кг." + '\n' + f"Мука - {round(int(message.text) * 0.13 / 10), 3} кг." + '\n' + f"Масло - {round(int(message.text) * 0.13 / 33), 3} кг." + '\n' + f"Томат - {round(int(message.text) * 0.13 / 3 / 6.6), 3} банок.")
    except Exception:
        await message.answer("Такого колличества я не знаю")

# ---------------------------------------------------------------------------------------- ВАРКА --------------------------------------------------------------------------------------------------------

@dp.message_handler(text=[str(i) for i in func.check_value()])
async def get_Varka(message: types.Message):
    num = ''
    for i in message.text:
        if i.isdigit():
            num += i
    await message.answer(func.check_value_state(message.text))
#------------------------------------------------------------------------------------------ОСТАТКИ-------------------------------------------------------------------------------------------------------
@dp.message_handler(commands=['add'])
async def add(message: types.Message):
    db.ADD(message.text).get_add()
    await message.answer("Значение добавлено")

@dp.message_handler(text=['✍ Добавить', '📄 Вывести', '🗑 Очистить таблицу'])
async def get_add(message: types.Message):
    if message.text == "✍ Добавить":
        await bot.send_message(message.chat.id, "Введите команду /add после чего остаток")
    elif message.text == '📄 Вывести':
        st = db.ADD().set_output()
        if len(st) != 0:
            await message.answer(db.ADD().set_output() + "\nЗначения показаны в килограммах")
        else:
            await message.answer("В таблице нет значений")
    elif message.text == '🗑 Очистить таблицу':
        db.ADD().data_delete()
        await message.answer("Значения удалены")

#-----------------------------------------------------------------------------------------СЕБЕСТОИМОСТЬ-----------------------------------------------------------------------------------------------------
@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    db.BUY(message.text).get_add()
    await message.answer("Значение добавлено")


@dp.message_handler(commands=['price'])
async def return_price(message: types.Message):
    await message.answer(str(db.BUY(message.text).get_output())+' руб')



@dp.message_handler(text=['💵 Цена', '🧮 Посчитать','📃 Показать данные', '🗑 Удалить'])
async def price(message: types.Message):
    if message.text == "💵 Цена":
        await bot.send_message(message.chat.id, "Введите команду /buy после чего остаток")
    elif message.text == "📃 Показать данные":
        st = db.BUY().set_output()
        if len(st) != 0:
            await message.answer(db.BUY().set_output() + "\nЗначения показаны в рублях")
        else:
            await message.answer("В таблице нет значений")
    elif message.text == '🧮 Посчитать':
        try:
            await message.answer("Введите команду /price после колличество штук сделано за месяц")
        except Exception:
            await message.answer("В таблице нет значений")
    elif message.text == '🗑 Удалить':
        db.BUY().data_delete()
        await message.answer("Значения удалены")

#-----------------------------------------------------------------------------------------ЗАКУПКА-----------------------------------------------------------------------------------------------------------

@dp.message_handler(text=['⬆ Главное меню', '📦 Воронеж', "📦 Новороссийск", "🥣 Варка", "✎ Остаток", "💲 Стоимость ингредиентов"])
async def bot_button(message: types.message):
    if message.text == "⬆ Главное меню":
        await bot.send_message(message.chat.id,"Главное меню", reply_markup=nav.mainMenu)
    if message.text == "📦 Воронеж":
        await bot.send_message(message.chat.id, 'Введите колличество штук', reply_markup=nav.otherMenu)
    elif message.text == "📦 Новороссийск":
        await message.answer("Сметана : 60 кг\n Масло : 1 упаковка\n Мука : 30 кг\n Томат : 2 банки")
    elif message.text == "🥣 Варка":
        await bot.send_message(message.chat.id, "Введите вид соуса и колличество штук\n", reply_markup=nav.btn_type_of_sauce)
    elif message.text == "✎ Остаток":
        await bot.send_message(message.chat.id, "Выберете действие", reply_markup=nav.btn_input_output)
    elif message.text == "💲 Стоимость ингредиентов":
        await bot.send_message(message.chat.id, "Выберете действие", reply_markup=nav.btnPriceInputOutput)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
