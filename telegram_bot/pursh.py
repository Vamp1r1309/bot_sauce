import main
import markups as nav
import time
time.sleep(10)
# --- Колличество 1 до 10000 шт ---
@main.dp.message_handler(text=[str(i) for i in range(1, 10000, 1)])
async def get_Voronezj(message: main.types.Message, ):
    await main.bot.send_message(message.chat.id, 'Введите колличество штук', reply_markup=nav.otherMenu)
    try:
        await message.answer(f"Сметана - {round(int(message.text) * 0.13 / 2.2), 3} кг." + '\n' + f"Мука - {round(int(message.text) * 0.13 / 10), 3} кг." + '\n' + f"Масло - {round(int(message.text) * 0.13 / 33), 3} кг." + '\n' + f"Томат - {round(int(message.text) * 0.13 / 3 / 6.6), 3} банок.")
    except Exception:
        await message.answer("Такого колличества я не знаю")
