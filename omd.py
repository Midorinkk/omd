from numpy.random import choice
from tqdm import tqdm
import time


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def check_weather():
    weather_types = ['\U0001F31E Ясно', '\U0001F327 Дождь',
                     '\U0001F32A Ураган']
    weather_weights = [0.4, 0.4, 0.2]

    for i in tqdm(range(10),
                  bar_format='\U0001F440 Считываем прогноз погоды: {bar}'):
        time.sleep(0.4)
    weather = choice(weather_types, p=weather_weights)
    print(f'Будет {weather}')
    return weather


def continious_action(action: str):
    print(action, end=' ')
    for _ in range(3):
        print('.', end=' ')
        time.sleep(0.7)
    print()


def huricane(umbrella: bool):
    continious_action('Утку-маляра 🦆 уносит ураган')
    if umbrella:
        print('Благодаря зонту она приземлилась прямо в бар.',
              'Весь вечер она пила пиво и веселилась \U0001F973')
    else:
        print('Она облетела весь город и вернулась домой.',
              'На сегодня пиво отменяется \U0001F625')


def step2_umbrella():
    weather = check_weather()
    continious_action('Утка-маляр 🦆 идёт в бар')
    if weather == '\U0001F31E Ясно':
        print('Утка-маляр 🦆 недовольна, что зря взяла зонт.',
              'Весь вечер она грустно пила пиво в одиночестве \U0001F629')
    elif weather == '\U0001F327 Дождь':
        print('Утка-маляр 🦆 счастлива, что не промокла.',
              'В баре она завела друзей, они вместе выпили', end=' ')
        print('\U0001F37B и пошли домой под её зонтом')
    else:
        huricane(True)


def step2_no_umbrella():
    weather = check_weather()
    continious_action('Утка-маляр 🦆 идёт в бар')
    if weather == '\U0001F31E Ясно':
        print('Утка-маляр 🦆 рада солнечному деньку.',
              'Она решила просто полгулять и не пошла в бар \U00002600')
    elif weather == '\U0001F327 Дождь':
        print('Утка-маляр 🦆 промокла до нитки.',
              'В баре над ней посмеялись, но дали бесплатное пиво 📈')
    else:
        huricane(False)


if __name__ == '__main__':
    step1()
