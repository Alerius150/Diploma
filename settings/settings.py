"""
Файл содержащий базовые конфигурации бота и API (Токен, API-ключ, заголовок, параметры и url-адреса)
"""

import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Файл .env отсутствует')
else:
    load_dotenv()

TOKEN = os.environ.get('TOKEN')
RAPIDAPI_KEY = os.environ.get('API_KEY')


HEADERS = {
    'X-RapidAPI-Host': 'hotels4.p.rapidapi.com',
    'X-RapidAPI-Key': RAPIDAPI_KEY
}


URL_SEARCH = 'https://hotels4.p.rapidapi.com/locations/v2/search'
URL_PROPERTY_LIST = 'https://hotels4.p.rapidapi.com/properties/v2/list'
URL_PHOTO = 'https://hotels4.p.rapidapi.com/properties/get-hotel-photos'
URL_HOTEL = 'https://www.hotels.com/ho{}'


QUERY_SEARCH = {
  'query': 'new_york',
  'locale': 'en_US',
  'currency': 'USD'
}

QUERY_PROPERTY_LIST = {
  'currency': 'USD',
  'eapid': 1,
  'locale': 'ru_RU',
  'siteId': 300000001,
  'destination': {'regionId': '2621'},
  'checkInDate': {
    'day': 10,
    'month': 10,
    'year': 2023
  },
  'checkOutDate': {
    'day': 15,
    'month': 10,
    'year': 2023
  },
  'rooms': [{'adults': 1}],
  'resultsStartingIndex': 0,
  'resultsSize': 200,
  'sort': 'PRICE_LOW_TO_HIGH',
  'filters': {'price': {
    'max': 11000,
    'min': 1
  }}
}
QUERY_CUSTOM =  {
  'currency': 'USD',
  'eapid': 1,
  'locale': 'ru_RU',
  'siteId': 300000001,
  'destination': {'regionId': '2621'},
  'checkInDate': {
    'day': 10,
    'month': 10,
    'year': 2023
  },
  'checkOutDate': {
    'day': 15,
    'month': 10,
    'year': 2023
  },
  'rooms': [{'adults': 1}],
  'resultsStartingIndex': 0,
  'resultsSize': 200,
  'sort': 'PRICE_LOW_TO_HIGH',
  'filters': {'price': {
    'max': 11000,
    'min': 1
  }}
}

QUERY_PHOTO = {'id': '1178275040'}