#!/usr/bin/env python
# -*- coding: utf-8 -*-

goods = {}

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

table_code = goods['Стол']
table_item_1 = store[table_code][0]
table_item_2 = store[table_code][1]
table_quantity_1 = table_item_1['quantity']
table_quantity_2 = table_item_2['quantity']
table_quantity = table_quantity_1 + table_quantity_2
table_price_1 = table_item_1['price']
table_price_2 = table_item_2['price']
table_cost = (table_quantity_1 * table_price_1) + (table_quantity_2 * table_price_2)
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

divan_code = goods['Диван']
divan_item_1 = store[divan_code][0]
divan_item_2 = store[divan_code][1]
divan_quantity_1 = divan_item_1['quantity']
divan_quantity_2 = divan_item_2['quantity']
divan_quantity = divan_quantity_1 + divan_quantity_2
divan_price_1 = divan_item_1['price']
divan_price_2 = divan_item_2['price']
divan_cost = (divan_quantity_1 * divan_price_1) + (divan_quantity_2 * divan_price_2)
print('Диван -', divan_quantity, 'шт, стоимость', divan_cost, 'руб')

stool_code = goods['Стул']
stool_item_1 = store[stool_code][0]
stool_item_2 = store[stool_code][1]
stool_item_3 = store[stool_code][2]
stool_quantity_1 = stool_item_1['quantity']
stool_quantity_2 = stool_item_2['quantity']
stool_quantity_3 = stool_item_3['quantity']
stool_quantity = stool_quantity_1 + stool_quantity_2 + stool_quantity_3
stool_price_1 = stool_item_1['price']
stool_price_2 = stool_item_2['price']
stool_price_3 = stool_item_3['price']
stool_cost = (stool_quantity_1 * stool_price_1) + (stool_quantity_2 * stool_price_2) + (stool_quantity_3 * stool_price_3)
print('Стул -', stool_quantity, 'шт, стоимость', stool_cost, 'руб')


for title, code in goods.items():  # Используем функцию .items() для получения ключа и значения  из словаря goods.
    total_quantity = 0  # Создаем переменную накопитель количества товаров.
    total_cost = 0  # Создаем переменную накопитель стоимости товаров.
    for goods in store[code]:
        total_quantity += goods['quantity']
        total_cost += goods['price'] * goods['quantity']

    print(title, " - ", total_quantity, " шт, ", 'стоимость', total_cost, " руб")


##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






