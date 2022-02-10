from requests import get
from bs4 import BeautifulSoup
from datetime import datetime


def currency_rates(curr_id):
    cur_out = {}
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    soup = BeautifulSoup(response.text, 'lxml')
    date = datetime.date(datetime.strptime(soup.valcurs['date'], "%d.%m.%Y"))
    currency_name = soup.find_all('charcode')
    currency_value = soup.find_all('value')
    for i in range(len(currency_name)):
        cur_out[str(currency_name[i].text)] = float(currency_value[i].text.replace(',', '.'))
    if curr_id.upper() not in cur_out.keys():
        return print('неверный идентификатор валюты')
    else:
        return print(f'На {date} курс {curr_id.upper()} равен {cur_out.get(curr_id.upper())} рубля')


currency_rates('вфывыфв')
currency_rates('eUr')
currency_rates('USD')