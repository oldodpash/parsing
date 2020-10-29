import requests


def info(vin):
    data = requests.post("request_url", data = {'vin': vin})
    return data.text


def update(vin):
    vin = vin.replace('У', 'Y').replace('А', 'A').replace('Т', 'T').\
        replace('Н', 'H').replace('В', 'B').replace('К', 'K')
    vin = vin.replace('Х', 'X').replace('О', '0').replace('O', '0').\
        replace('С', 'C').replace('М', 'M').replace('Р', 'P').replace('Е', 'E')
    vin = vin.replace('text:', '').replace('"', '').replace("'", '')
    return vin


def start(vin):
    try:
        answer = info(update(vin))
        print(answer)
        if len(answer) <= 71:
            answer = 'отзывные компании не найдены.'
        else:
            answer = 'найдены отзывные компании.'
    except Exception:
        answer = 'информация о наличии отзывных компаниях не была получена.'
    return f'Статус отзывных компаний: {answer}'
