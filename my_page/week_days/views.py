from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
weeks = {
    'monday': 'Понедельник день бездельник',
    'tuesday': 'Вторник повторник',
    'wednesday': 'Среда-тамада',
    'thursday': 'Четверг-я заботы все отверг',
    'friday': 'Пятница-пьяница',
    'saturday': 'Суббота-безработа',
    'sunday': 'Воскресенье-день веселья!',
}


# Create your views here.
def weeks_day_info(request, day_info):
    description = weeks.get(day_info)
    return render(request,'week_days/greeting.html')



def weeks_day_info_to_number(request, day_info):
    if day_info > 7 or day_info < 1:
        return HttpResponseNotFound(f'Неверный номер дня недели - {day_info}')
    description = list(weeks)[day_info - 1]
    redirect_url = reverse('days', args=(description,))
    return HttpResponseRedirect(redirect_url)


def days_list(request):
    days = list(weeks)
    rez_str = ''
    for i in days:
        redirect_url = reverse('days', args=(i,))
        rez_str += f'<li><a href = {redirect_url}>{i.title()}</a></li>'
    final = f'''
    <ul>
        {rez_str}
    </ul>
    '''
    return HttpResponse(final)
