import requests
from bs4 import BeautifulSoup


def update(vin):
    vin = vin.replace('У', 'Y').replace('А', 'A').replace('Т', 'T'). \
        replace('Н', 'H').replace('В', 'B').replace('К', 'K')
    vin = vin.replace('Х', 'X').replace('О', '0').replace('O', '0'). \
        replace('С', 'C').replace('М', 'M').replace('Р', 'P').replace('Е', 'E')
    vin = vin.replace('text:', '').replace('"', '').replace("'", '')
    return vin


def parsing(vin):
    url = 'request_url'
    try:
        r = requests.get(url, data={'vin': str(vin)}, verify=False)
        soup = BeautifulSoup(r.text, 'lxml')
        tables = soup.find_all('div', {'class': 'vin-check__card-info'})
        date = tables[-1].text.strip()
    except Exception:
        date = 'нет данных'
    return {'vin': vin, 'date': date}


def start(vin):
    answer = parsing(update(vin))
    return f'ФТС Дата выпуска: {answer["date"]}.'

#print(start('CHSD23AAJG1001961'))