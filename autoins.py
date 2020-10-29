import json
import requests


def make_request(id_str, mmm):
    headers = {
        'mobileAppLogin': 'rsa_mp_android',
        'mobileAppPassword': 'G87hd9*^&ol&V8998p)*&_#!',
        'Content-Type': 'Application/json'
    }
    payload = {
        'guid': '9DC3B6606CE54A9D82A24A3A57CF75E6',
        'policyNumberKey': id_str,
        'policySerialKey': mmm,
        'userId': 299789
    }
    api_url = 'request_url'
    request = requests.post(api_url, data=json.dumps(payload), headers=headers)
    return request.json()


def main(ab):
    print('--- Проверка по осаго Autoins ---')
    print('Осаго:', ab)
    osago_series = ab[:3].upper().replace('P', 'Р').replace('K', 'К').replace('M', 'М').replace('E', 'Е').replace('X', 'Х')\
        .replace('A', 'А').replace('C', 'С').replace('B', 'В').replace('H', 'Н')
    osago_number = ab[4::]
    try:
        a = make_request(osago_number, osago_series)['policyInfoExtended'][0]
        additional_phrase = ''
        if a['period1Beg'] != None and a['period1End'] != None:
            additional_phrase += f'Период использования №1: {a["period1Beg"]} - {a["period1End"]}\n'
        if a['period2Beg'] != None and a['period2End'] != None:
            additional_phrase += f'Период использования №2: {a["period2Beg"]} - {a["period2End"]}\n'
        if a['period3Beg'] != None and a['period3End'] != None:
            additional_phrase += f'Период использования №3: {a["period3Beg"]} - {a["period3End"]}\n'
        return str(f'Оформлен: {a["dateCreate"]},\nСрок страхования с: {a["dateActionBeg"]} - {a["dateActionEnd"]},\n' \
              + additional_phrase).replace('None', '-').strip()
    except Exception:
        return ''
