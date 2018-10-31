# -*- coding: utf-8 -*-

# Подключаем модули
import requests, bs4, datetime

# Создаем переменную с кодом страницы для парсинга
url = requests.get('https://ru.aliexpress.com/item/BESDER-H-264-ONVIF-POE-48V-4CH-1080P-NVR-Recorder-P2P-Motion-Detect-Alarm-Security-Surveillance/32830343826.html')

# Создаем объект с данными из переменной
data = bs4.BeautifulSoup(url.text, "html.parser")

# Описываем что нужно получить со страницы
name_arr = data.select('#j-product-detail-bd > div.detail-main > div > h1')
price_on_discont_arr = data.select('#j-sku-discount-price')

# Полученый результат сохраним в переменные
name = name_arr[0].getText()
price_on_discont = price_on_discont_arr[0].getText()

# Текущая дата и время
now = datetime.datetime.now()
curent_datetime = now.strftime("%d-%m-%Y %H:%M")

# Запишем результат в файл
f = open('result.txt', 'a', encoding='utf-8')
f.write(curent_datetime + "|" + name + "|" + price_on_discont + "\n")
f.close()