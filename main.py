import telebot
import requests
from config import TOKEN
from keyboards import keyboard
from recipe import BREAKFAST
from recipe import LUNCH
from recipe import DINNER

users = {}

bot = telebot.TeleBot(TOKEN, parse_mode = "html")

@bot.message_handler(commands = ["start"])


def start(message):
    users[message.chat.id] = {}
    bot.send_message(message.chat.id, "Привет, я бот, который поможет подобрать рецепт📃")
    bot.send_message(message.chat.id, "Выберете приём пищи:", reply_markup = keyboard("Завтрак🧇", "Обед🥣", "Ужин🥘"))
    bot.register_next_step_handler(message, mealtime)


def mealtime(message):
    if message.text == "Завтрак🧇":
        users[message.chat.id]["type"] = "breakfast"
        bot.send_message(message.chat.id, "Выберете тип пищи:", reply_markup = keyboard("Сладкое🍬", "Солёное🧂"))
        bot.register_next_step_handler(message, breakfast)
    elif message.text == "Обед🥣":
        users[message.chat.id]["type"] = "lunch"
        bot.send_message(message.chat.id, "Выберете тип блюда:", reply_markup = keyboard("1-ое блюдо🍲", "2-ое блюдо🍝"))
        bot.register_next_step_handler(message, lunch)
    elif message.text == "Ужин🥘":
        users[message.chat.id]["type"] = "dinner"
        bot.send_message(message.chat.id, "Выберете тип блюда:", reply_markup=keyboard("Мясное🥩", "Рыбное🐟", "Гарнир🍚"))
        bot.register_next_step_handler(message, dinner)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")


def breakfast(message):
    if message.text == "Сладкое🍬":
        users[message.chat.id]["category"] = "sweet"
        bot.send_message(message.chat.id, "Выберете тип пищи:", reply_markup=keyboard("Из творога🍮", "Из теста🥞", "Каша🍚"))
        bot.register_next_step_handler(message, sweet_breakfast)
    elif message.text == "Солёное🧂":
        users[message.chat.id]["category"] = "salty"
        bot.send_message(message.chat.id, "Выберете тип пищи:", reply_markup=keyboard("Из яиц🍳", "Сэндвич🥪"))
        bot.register_next_step_handler(message, salty_breakfast)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")

def lunch(message):
    if message.text == "1-ое блюдо🍲":
        users[message.chat.id]["category"] = "first_course"
        bot.send_message(message.chat.id, "Выберете тип пищи:", reply_markup=keyboard("Холодный суп🧊", "Горячий суп♨", "Крем-суп"))
        bot.register_next_step_handler(message, first_course)
    elif message.text == "2-ое блюдо🍝":
        users[message.chat.id]["category"] = "second_course"
        bot.send_message(message.chat.id, "Выберете тип пищи:", reply_markup=keyboard("Из мяса🥩", "Из рыбы🐟", "Из птицы🐔", "Гарнир🍚"))
        bot.register_next_step_handler(message, second_course)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")

def dinner(message):
    if message.text == "Мясное🥩":
        users[message.chat.id]["category"] = "meat"
        bot.send_message(message.chat.id, "Выберете тип пищи:", reply_markup=keyboard("Острое🌶", "Неострое"))
        bot.register_next_step_handler(message, meat_dinner)
    elif message.text == "Рыбное🐟":
        users[message.chat.id]["category"] = "fish"
        bot.send_message(message.chat.id, "Выберете тип пищи:", reply_markup=keyboard("Острое🌶", "Неострое"))
        bot.register_next_step_handler(message, fish_dinner)
    elif message.text == "Гарнир🍚":
        users[message.chat.id]["category"] = "garnish"
        bot.send_message(message.chat.id, "Выберете тип пищи:", reply_markup=keyboard("Острое🌶", "Неострое"))
        bot.register_next_step_handler(message, garnish)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")


def sweet_breakfast(message):
    if message.text == "Из творога🍮":
        users[message.chat.id]["subcategory"] = "curd"
        recipes = BREAKFAST.get("sweet").get("curd")
        titles = list(map(lambda recipe:recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Из теста🥞":
        users[message.chat.id]["subcategory"] = "dough"
        recipes = BREAKFAST.get("sweet").get("dough")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Каша🍚":
        users[message.chat.id]["subcategory"] = "porridge"
        recipes = BREAKFAST.get("sweet").get("porridge")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")


def salty_breakfast(message):
    if message.text == "Из яиц🍳":
        users[message.chat.id]["subcategory"] = "egg"
        recipes = BREAKFAST.get("salty").get("egg")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Сэндвич🥪":
        users[message.chat.id]["subcategory"] = "sandwich"
        recipes = BREAKFAST.get("salty").get("sandwich")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")


def first_course(message):
    if message.text == "Холодный суп🧊":
        users[message.chat.id]["subcategory"] = "cold"
        recipes = LUNCH.get("first_course").get("cold")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Горячий суп♨":
        users[message.chat.id]["subcategory"] = "hot"
        recipes = LUNCH.get("first_course").get("hot")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Крем-суп":
        users[message.chat.id]["subcategory"] = "cream-soup"
        recipes = LUNCH.get("first_course").get("cream-soup")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")


def second_course(message):
    if message.text == "Из мяса🥩":
        users[message.chat.id]["subcategory"] = "meat"
        recipes = LUNCH.get("second_course").get("meat")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Из рыбы🐟":
        users[message.chat.id]["subcategory"] = "fish"
        recipes = LUNCH.get("second_course").get("fish")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Из птицы🐔":
        users[message.chat.id]["subcategory"] = "bird"
        recipes = LUNCH.get("second_course").get("bird")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Гарнир🍚":
        users[message.chat.id]["subcategory"] = "garnish"
        recipes = LUNCH.get("second_course").get("garnish")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")


def meat_dinner(message):
    if message.text == "Острое🌶":
        users[message.chat.id]["subcategory"] = "chilly"
        recipes = DINNER.get("meat").get("chilly")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Неострое":
        users[message.chat.id]["subcategory"] = "not_chilly"
        recipes = DINNER.get("meat").get("not_chilly")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")

def fish_dinner(message):
    if message.text == "Острое🌶":
        users[message.chat.id]["subcategory"] = "chilly"
        recipes = DINNER.get("fish").get("chilly")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Неострое":
        users[message.chat.id]["subcategory"] = "not_chilly"
        recipes = DINNER.get("fish").get("not_chilly")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")

def garnish(message):
    if message.text == "Острое🌶":
        users[message.chat.id]["subcategory"] = "hot"
        recipes = DINNER.get("garnish").get("hot")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    elif message.text == "Неострое":
        users[message.chat.id]["subcategory"] = "not_chilly"
        recipes = DINNER.get("garnish").get("not_chilly")
        titles = list(map(lambda recipe: recipe.get("title"), recipes))
        bot.send_message(message.chat.id, "Выберете рецепт:", reply_markup=keyboard(*titles))
        bot.register_next_step_handler(message, send_recipes)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю🤔")


def send_recipes(message):
    print(users)
    user = users[message.chat.id]
    if user["type"] == "breakfast":
        recipes = BREAKFAST.get(user.get("category")).get(user.get("subcategory"))
        recipe = list(filter(lambda recipe: recipe["title"] == message.text, recipes))[0]
        image = requests.get(recipe["image"])
        caption = f"<b>{recipe.get('title')}</b>\n\n" \
                  f"{' '.join(recipe.get('ingredients'))}"
        bot.send_photo(message.chat.id, image.content, caption=caption)
        bot.send_message(message.chat.id, '\n\n'.join(recipe.get('steps')))
    if user["type"] == "lunch":
        recipes = LUNCH.get(user.get("category")).get(user.get("subcategory"))
        recipe = list(filter(lambda recipe: recipe["title"] == message.text, recipes))[0]
        image = requests.get(recipe["image"])
        caption = f"<b>{recipe.get('title')}</b>\n\n" \
                  f"{' '.join(recipe.get('ingredients'))}"
        bot.send_photo(message.chat.id, image.content, caption=caption)
        bot.send_message(message.chat.id, '\n\n'.join(recipe.get('steps')))
    if user["type"] == "dinner":
        recipes =DINNER.get(user.get("category")).get(user.get("subcategory"))
        recipe = list(filter(lambda recipe: recipe["title"] == message.text, recipes))[0]
        image = requests.get(recipe["image"])
        caption = f"<b>{recipe.get('title')}</b>\n\n" \
                  f"{' '.join(recipe.get('ingredients'))}"
        bot.send_photo(message.chat.id, image.content, caption=caption)
        bot.send_message(message.chat.id, '\n\n'.join(recipe.get('steps')))
    start(message)





bot.infinity_polling()