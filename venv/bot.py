# -*- coding: utf-8 -*-
#7b23e46911a09378e9e89aefb78294361c9d8a1331831bad16901d4c969f889e44a2f583ef9e5712873c9
import random, vk_api, vk
import logging
import threading
import time
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
vk_session = vk_api.VkApi(token='ff8895cc1ea1152cc791777bba683265a18454c45269abecc7d78e9cafef96f906e380bded43e0a610aa0')
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
longpoll = VkBotLongPoll(vk_session, 201836241)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType
Lslongpoll = VkLongPoll(vk_session)
Lsvk = vk_session.get_api()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Ассортимент', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Список городов', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=201836241")
'''
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if 'Ку' in str(event) or 'Привет' in str(event) or 'Хай' in str(event) or 'Хелло' in str(event) or 'Хеллоу' in str(event):
            if event.from_chat:
                vk.messages.send(
                    key = ('147ea3c3df9321785d11125a53653fb815454107'),          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = ('https://lp.vk.com/wh201836241'),
                    ts=('4'),
                    random_id = get_random_id(),
              	    message='Привет!',
            	    chat_id = event.chat_id
                    )
        if 'Клавиатура' in str(event):
            if event.from_chat:
                vk.messages.send(
                    keyboard = keyboard.get_keyboard(),
                    key = ('147ea3c3df9321785d11125a53653fb815454107'),          #ВСТАВИТЬ ПАРАМЕТРЫ
                    server = ('https://lp.vk.com/wh201836241'),
                    ts=('4'),
                    random_id = get_random_id(),
              	    message='Держи',
             	    chat_id = event.chat_id
            	    )
'''

def hello():
    time.sleep(5)
    Lsvk.messages.send(
        user_id=event.user_id,
        message='Привет!\n Если нужна помощь - так мне и напиши)',
        random_id=get_random_id()
    )

def menu():
    Lsvk.messages.send(
        user_id=event.user_id,
        message='Пицца "Маргарита" - 350p\n'
                'Пицца "Карбонара" - 380p\n'
                'Спагетти "Болоньезе" - 250p\n'
                'Морс 0.5л - 50p\n',
        random_id=get_random_id()
    )

def help():
    Lsvk.messages.send(
        user_id=event.user_id,
        message='Для вызова меню бота напишите в диалог кодовую фразу "Меню" или "Клавиатура"',
        random_id=get_random_id()
    )

def cities():
    Lsvk.messages.send(
        user_id=event.user_id,
        message='Астана\n'
                'Санкт-Петербург\n'
                'Великий Новгород',
        random_id=get_random_id()
    )

def keyboard():
    Lsvk.messages.send(
        user_id=event.user_id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message='Держи'
    )

for event in Lslongpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        vars1 = ['Привет', 'Ку', 'Хай', 'Хеллоу', 'привет', 'ку', 'хай', 'хеллоу']
        if event.text in vars1:
            if event.from_user:
                logging.info("First Thread start")
                x = threading.Thread(target=hello)
                x.start()
                logging.info("First Thread finish")

        if event.text == 'Ассортимент':
            if event.from_user:
                logging.info("Second Thread start")
                x = threading.Thread(target=menu)
                x.start()
                logging.info("Second Thread finish")

        vars3 = ['Помощь', 'помощь']
        if event.text in vars3:
            if event.from_user:
                if event.from_user:
                    x = threading.Thread(target=help)
                    x.start()

        if event.text == 'Список городов':
            if event.from_user:
                if event.from_user:
                    x = threading.Thread(target=cities)
                    x.start()

        vars2 = ['Клавиатура', 'клавиатура', 'Меню', 'меню']
        if event.text in vars2:
            if event.from_user:
                if event.from_user:
                    x = threading.Thread(target=keyboard)
                    x.start()