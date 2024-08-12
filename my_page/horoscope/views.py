from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля). Мой самый любимый знак зодиака.',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

type_zodiac_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


# Create your views here.
def get_info_about_sign_zodiac(request, sign_zodiac):
    description = zodiac_dict.get(sign_zodiac)
    elem_list = list(zodiac_dict)
    zodiac_date = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict,
    }
    return render(request, 'horoscope/info_zodiac.html', context=zodiac_date)


def get_info_about_sign_zodiac_to_number(request, sign_zodiac):
    if sign_zodiac > 12 or sign_zodiac < 1:
        return HttpResponseNotFound('Передан неправильный порядковый номер знака зодиака')
    description = list(zodiac_dict)[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(description,))
    return HttpResponseRedirect(redirect_url)


def main_menu(request):
    elem_list = list(zodiac_dict)
    main_dict = {
        'zodiacs': zodiac_dict
    }
    return render(request, 'horoscope/main_menu.html', context=main_dict)


def get_zodiac_sign(month, day):
    zodiac_signs = [
        ('aries', 21, 3, 19, 4),
        ('taurus', 20, 4, 20, 5),
        ('gemini', 21, 5, 20, 6),
        ('cancer', 21, 6, 22, 7),
        ('leo', 23, 7, 22, 8),
        ('virgo', 23, 8, 22, 9),
        ('libra', 23, 9, 22, 10),
        ('scorpio', 23, 10, 21, 11),
        ('sagittarius', 22, 11, 21, 12),
        ('capricorn', 22, 12, 19, 1),
        ('aquarius', 20, 1, 18, 2),
        ('pisces', 19, 2, 20, 3),
    ]
    for sing, start_day, start_month, end_day, end_month in zodiac_signs:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sing


def is_valid_date(month, day):
    if month < 1 or month > 12:
        return False
    day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > day_in_month[month - 1]:
        return False
    return True


def zodiac_view(request, month: int, day: int):
    if is_valid_date(month, day):
        zodiac_signs_for_date = get_zodiac_sign(month, day)
        redirect_url = reverse('horoscope-name', args=(zodiac_signs_for_date,))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверная дата знака зодиака!!!')
