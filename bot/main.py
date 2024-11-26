import sys
import os

# Add the parent directory to sys.path so it can find the apis module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apis.secrets import API_BOT


import telebot
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from apis.secrets import API_BOT
from contex import *
from math import radians, sin, cos, sqrt, atan2

bot = telebot.TeleBot(API_BOT)
Soft_lat = 38.56401624794034
Soft_lon = 68.75892534477292

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth's radius in meters
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)

    a = sin(delta_phi / 2)**2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c  
    return distance

@bot.message_handler(commands=["start"])
def start_choice(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("I have arrived!")
    btn2 = KeyboardButton("I won't come today")
    btn3 = KeyboardButton("I am going home!")
    markup.row(btn1, btn2, btn3)

    markup2 = ReplyKeyboardMarkup(resize_keyboard=True)
    group = get_groups()
    for subject_name in group:
        btn = KeyboardButton(subject_name)
        markup2.add(btn)

    is_user_exist = get_student1(message.chat.id)
    if is_user_exist:
        if message.chat.username:
            save_students(message)
            is_not_group = get_student2(message.chat.id)
            if is_not_group:
                bot.send_message(message.chat.id, "Please, enter your group:", reply_markup=markup2)
                bot.register_next_step_handler(message, add_group)
        else:
            bot.send_message(message.chat.id, "You don't have a username. Please, enter one:")
            bot.register_next_step_handler(message, new_username)
    bot.send_message(message.chat.id, "Welcome to my bot! Please, choose one of these options!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "I have arrived!":
        is_user_exist = get_student(message.chat.id)
        if is_user_exist:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            location_button = KeyboardButton("Send my location", request_location=True)
            markup.add(location_button)
            bot.send_message(message.chat.id, "Please, send your location.", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "You have already been marked today!")
    elif message.text == "I won't come today":
        is_user_exist = get_student(message.chat.id)
        if is_user_exist:
            bot.send_message(message.chat.id, "Please, tell us the reason for your absence today.")
            bot.register_next_step_handler(message, prichina)
        else:
            bot.send_message(message.chat.id, "You have already been marked today!")
    elif message.text == "I am going home!":
        student = show_who_be1(message.chat.id)
        if True:
            update_out(message.chat.id)
            bot.send_message(message.chat.id, "See you tomorrow, and please don't be late!")
        else:
            bot.send_message(message.chat.id, "You have already been marked or didn't attend today!")

@bot.message_handler(content_types=["location"])
def handle_location(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("I have arrived!")
    btn2 = KeyboardButton("I won't come today")
    btn3 = KeyboardButton("I am going home!")
    markup.row(btn1, btn2, btn3)

    user_lat = message.location.latitude
    user_lon = message.location.longitude

    distance = calculate_distance(user_lat, user_lon, Soft_lat, Soft_lon)

    if distance <= 50:
        save_students_come(message)
        bot.send_message(message.chat.id, "Great job for arriving!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"You are not at Soft Club. You are {distance:.2f} meters away.", reply_markup=markup)

@bot.message_handler()
def ask_location(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    location_button = KeyboardButton("Send my location", request_location=True)
    markup.add(location_button)
    bot.send_message(message.chat.id, "Please, send your location.", reply_markup=markup)

def prichina(message):
    save_students_notcome(message, message.text)
    bot.send_message(message.chat.id, "Thank you for explaining why you cannot come today!")

def new_username(message):
    username = message.text
    save_students_come2(message, username) 
    bot.send_message(message.chat.id, "Thank you! Now you can use the bot :)")

def add_group(message):
    group = message.text
    update_user(message.chat.id, group)
    bot.send_message(message.chat.id, "Thank you! Now you can use the bot :)")

bot.infinity_polling()
