from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Main Menu ---

btnAmount = KeyboardButton("📦 Воронеж")
btnOther = KeyboardButton('📦 Новороссийск')
btnVar = KeyboardButton('🥣 Варка')
btnPrice = KeyboardButton('💲 Стоимость ингредиентов')
btnRemain = KeyboardButton('✎ Остаток')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAmount, btnPrice, btnVar, btnOther, btnRemain)


# --Exit Main Menu ---
btnMain = KeyboardButton("⬆ Главное меню")

otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)



# --- type of sauce ---

btn_cheece = KeyboardButton("🧀 Сырный")
btn_garlic = KeyboardButton("🧄 Чесночный")
btn_pomidor = KeyboardButton("🍅 Томатный")



btn_type_of_sauce = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMain)


btnOutput = KeyboardButton("📄 Вывести")
btnInput = KeyboardButton("✍ Добавить")
btnClear = KeyboardButton("🗑 Очистить таблицу")

btn_input_output = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInput, btnOutput, btnClear, btnMain)


#---------------------PRICE-------------------------------------------

btnAdd = KeyboardButton("💵 Цена")
btnsell = KeyboardButton("🧮 Посчитать")
btnDel = KeyboardButton("🗑 Удалить")
btnSetter = KeyboardButton("📃 Показать данные")

btnPriceInputOutput = ReplyKeyboardMarkup(resize_keyboard=True).add(btnAdd, btnsell, btnDel, btnSetter, btnMain)
