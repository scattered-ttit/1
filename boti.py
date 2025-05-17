import telebot
import requests
import json
import random

TOKEN = '7599952576:AAEnlxn13RvjfNax8DjBG4qeR2rmhSXGEuQ'
bot = telebot.TeleBot(TOKEN)

# Клавиатура
menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row('😺 Котик', '🌦 Погода')
menu.row('🧮 Калькулятор', '🎲 Рандом')

# ========== 1. КОТ ========== #
def get_cat_image_url():
    r = requests.get('https://api.thecatapi.com/v1/images/search')
    return r.json()[0]['url']

# ========== 2. ПОГОДА ========== #
def get_weather(city):
    API_KEY = '1a928110d26c4bc652bfd7f69580fd7b'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'appid': API_KEY,
        'q': city,
        'units': 'metric',
        'lang': 'ru'}
    res = requests.get(base_url, params=params)
    if res.status_code == 200:
        data = res.json()
        return f"🌤 Погода в {city}:\nТемпература: {data['main']['temp']}°C\n{data['weather'][0]['description']}"
    else:
        return '⚠️ Город не найден!'

# ========== 3. КАЛЬКУЛЯТОР ========== #
def simple_calc(expr):
    try:
        return f"🧮 Результат: {eval(expr)}"
    except:
        return '⚠️ Ошибка выражения!'

# ========== 4. АВТОРИЗАЦИЯ ========== #
auth_data = {}
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Привет! Я Зелецель. Выберите действие:", reply_markup=menu)

@bot.message_handler(func=lambda m: m.text == '😺 Котик')
def send_cat(message):
    bot.send_photo(message.chat.id, photo=get_cat_image_url())

@bot.message_handler(func=lambda m: m.text == '🌦 Погода')
def ask_city(message):
    msg = bot.send_message(message.chat.id, 'Введите название города:')
    bot.register_next_step_handler(msg, send_weather)

def send_weather(message):
    result = get_weather(message.text)
    bot.send_message(message.chat.id, result)

@bot.message_handler(func=lambda m: m.text == '🧮 Калькулятор')
def ask_expr(message):
    msg = bot.send_message(message.chat.id, 'Введите выражение (например: 2 + 2 * 5):')
    bot.register_next_step_handler(msg, calc_result)

def calc_result(message):
    bot.send_message(message.chat.id, simple_calc(message.text))

@bot.message_handler(func=lambda m: m.text == '🎲 Рандом')
def random_number(message):
    number = random.randint(1, 100)
    bot.send_message(message.chat.id, f'🎲 Ваше случайное число: {number}')


# ========== ПУСК ========== #
print("Бот запущен...")
bot.polling(non_stop=True)
