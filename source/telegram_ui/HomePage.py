import telebot
from telebot import  types
from elements import Buttons
import config


bot = telebot.TeleBot('1259898554:AAESwC2gAWQ1Z4nE0Z2fNylLdEraLq-iL5A')


@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id,"Привет, ты написал мне /start", reply_markup=Buttons.main_keyboard())

@bot.callback_query_handler(func = lambda call :True)
def input_sum(call):
    if call.data == "hand_waste":
        bot.answer_callback_query(
            call.id,
            text="koko")
        msg = bot.send_message(call.message.chat.id, "Внесіть суму витрати: ")
        bot.register_next_step_handler(message=msg, callback= enter_sum)
        # @bot.message_handler(content_types=['text'])
        # def ff(message):


    if call.data == "seek_waste":
        pass

    if call.data == "food":
        waste_info = f"Витрата додана\n{Buttons.food.text}\n{price_num} грн."
        bot.send_message(call.message.chat.id, waste_info)



# @bot.message_handler(content_types=['text'])

def enter_sum(message):
    if not message.text.isdigit():
        number = bot.send_message(message.chat.id, "Введите плез число")
        bot.register_next_step_handler(message=number, callback=enter_sum)
        return
    global price_num
    price_num = message.text
    bot.send_message(message.chat.id, "Choose category", reply_markup=Buttons.choose_category())

def enter_category(category):
    pass
def input_money():
    name = bot.message_handler(content_types=['text'])
    print(name)

if __name__ == "__main__":
    bot.polling()

