from django.shortcuts import render
from .models import *
from .forms import CaseForm
from registration.models import *
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime, time, timedelta

def calc_time(start, end):
    end = timedelta(hours=end.hour, minutes=end.minute)
    start = timedelta(hours=start.hour, minutes=start.minute)
    return int((end - start).seconds / 3600)

def data_generation(request, data, day, day_short):
    cases_tmp = [case for case in data]
    cases_sorted_by_time = []
    while len(cases_tmp) != 0:
        min_ = -1
        for case in cases_tmp:
            if case.case_start.hour < min_ or min_ == -1:
                min_ = case.case_start.hour
                to_del = case
        cases_sorted_by_time.append(to_del)
        print(to_del.case_start)
        try:
            cases_tmp.remove(to_del)
        except:
            pass
    day_data = []
    busy_time = 0
    free_time = 24
    counter = 0
    for case in cases_sorted_by_time:
        tmp = []
        counter += 1
        tmp.append(case.case)  # Задача
        tmp.append(case.case_description)  # Описание задачи
        tmp.append(calc_time(case.case_start, case.case_end))  # Длительность
        tmp.append(case.case_start.hour)  # начало
        tmp.append(case.case_end.hour)  # конец
        tmp.append(case.id) # id
        tmp.append(counter)
        day_data.append(tmp)
        busy_time += calc_time(case.case_start, case.case_end)
    progress_bar = int((busy_time/24)*100)

    try:
        user = request.session['user_name']
    except KeyError:
        user = "None"

    return {
        'day_short' : day_short,
        'day' : day,
        "cases" : day_data,
        "busy_time" : busy_time,
        "empty_time" : free_time-busy_time,
        "progress": progress_bar,
        "user" : user,
        "cases_count" : len(cases_sorted_by_time),
    }

def profile(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    monday_data = Monday.objects.filter(user=user_tmp.id, is_default=False)
    return render(request, "webcalendar/profile.html", context=data_generation(request,monday_data, 'Monday', 'mnd'))

def monday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Monday.objects.filter(user=user_tmp.id, is_default=False)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Monday', 'mnd'))

def tuesday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Tuesday.objects.filter(user=user_tmp.id, is_default=False)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Tuesday', 'tue'))

def wednesday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Wednesday.objects.filter(user=user_tmp.id, is_default=False)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Wednesday', 'wed'))

def thursday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Thursday.objects.filter(user=user_tmp.id, is_default=False)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Thursday', 'thu'))

def friday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Friday.objects.filter(user=user_tmp.id, is_default=False)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Friday', 'fri'))

def saturday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Saturday.objects.filter(user=user_tmp.id, is_default=False)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Saturday', 'sat'))

def sunday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Sunday.objects.filter(user=user_tmp.id, is_default=False)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Sunday', 'sun'))

def get_day(day_short):
    if day_short == 'mnd':
        day = Monday
    elif day_short == 'tue':
        day = Tuesday
    elif day_short == 'wed':
        day = Wednesday
    elif day_short == 'thu':
        day = Thursday
    elif day_short == 'fri':
        day = Friday
    elif day_short == 'sat':
        day = Saturday
    elif day_short == 'sun':
        day = Sunday
    else: raise Exception('Неизвестное day_short')
    return day

def add_case(request, day_short=''):
    if request.method == "GET":
        caseForm = CaseForm()
        data = {
            'form' : CaseForm, 
            'day_short' : day_short
            }
        return render(request, "webcalendar/addcase.html", context=data)

    elif request.method == "POST":
        start = request.POST.get('case_start')
        end = request.POST.get('case_end')
        case_name = request.POST.get('case')
        description = request.POST.get('case_description')
        user_tmp = User.objects.get(user_name=request.session['current_user'])

        day = get_day(day_short)
        cases = day.objects.filter(user=user_tmp)

        new_start_hrs = int(start[0:2])
        new_end_hrs = int(end[0:2])
        if new_start_hrs >= new_end_hrs: return HttpResponse("Start should be less then end. Лучше конечно проверку на js сделать👍👍👍")
        #if new_start_hrs >= new_end_hrs: return HttpResponse("<script>alert('Start should be less then end. Лучше конечно проверку на js сделать👍👍👍')<script>")
        if new_start_hrs < 0 or new_start_hrs > 23: return HttpResponse("Wrong time start_case. Лучше конечно проверку на js сделать👍👍👍")
        if new_end_hrs < 0 or new_end_hrs > 23: return HttpResponse("Wrong time end_case. Лучше конечно проверку на js сделать👍👍👍")

        for case in cases:
            old_start_hrs = case.case_start.hour
            old_end_hrs = case.case_end.hour
            if not (old_start_hrs >= new_end_hrs or old_end_hrs <= new_start_hrs): # проверка на конфликт дел по времени
                return HttpResponse('Ошибка. новое дело конфликтует со старым. потом перестилизуешь👍👍👍')
        day.objects.create(user=user_tmp, case_start=start, case_end=end, case=case_name, case_description=description, is_default=False)

        return HttpResponseRedirect("/profile/"+day_short)

def set_default(request, day_short):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    day = get_day(day_short)
    # удаление дефолтных дел, которые устарели и должны поменяться на новые
    cases = day.objects.filter(user=user_tmp, is_default=True)
    for case in cases:
        case.delete()

    # задание новых дефолтных дел
    cases = day.objects.filter(user=user_tmp, is_default=False)
    for case in cases:
        day.objects.create(user=user_tmp, case_start=case.case_start, case_end=case.case_end, case=case.case, case_description=case.case_description, is_default=True)

    return HttpResponseRedirect("/profile/"+day_short)

def reset_to_default(request, day_short=''):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    if day_short == '':
        days = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
    else:
        days = [get_day(day_short)]
    for day in days:
        # Удаление всех недефолтных дел
        cases = day.objects.filter(user=user_tmp, is_default=False)
        for case in cases:
            case.delete()
        # Заполнение дня дефолтными делами
        cases = day.objects.filter(user=user_tmp, is_default=True)
        for case in cases:
            day.objects.create(user=user_tmp, case_start=case.case_start, case_end=case.case_end, case=case.case, case_description=case.case_description, is_default=False)
    return HttpResponseRedirect("/profile/"+day_short)

def delete_case(request, day_short='', case_id=''):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    case = BaseDay.objects.get(id=case_id, user=user_tmp)
    case.delete()
    return HttpResponseRedirect("/profile/"+day_short)

def change_case(request, day_short, case_id):
    if request.method == "GET":
        caseForm = CaseForm()
        data = {'form' : caseForm, 'day_short' : day_short, 'case_id' : case_id }
        return render(request, "webcalendar/changecase.html", context=data)

    elif request.method == "POST":
        start = request.POST.get('case_start')
        end = request.POST.get('case_end')
        case_name = request.POST.get('case')
        description = request.POST.get('case_description')
        user_tmp = User.objects.get(user_name=request.session['current_user'])

        day = get_day(day_short)
        cases = day.objects.filter(user=user_tmp)

        new_start_hrs = int(start[0:2])
        new_end_hrs = int(end[0:2])
        if new_start_hrs >= new_end_hrs: return HttpResponse("Start should be less then end. Лучше конечно проверку на js сделать👍👍👍")
        if new_start_hrs < 0 or new_start_hrs > 23: return HttpResponse("Wrong time start_case. Лучше конечно проверку на js сделать👍👍👍")
        if new_end_hrs < 0 or new_end_hrs > 23: return HttpResponse("Wrong time end_case. Лучше конечно проверку на js сделать👍👍👍")

        for case in cases:
            if str(case.id) == case_id:
                continue
            old_start_hrs = case.case_start.hour
            old_end_hrs = case.case_end.hour
            if not (old_start_hrs >= new_end_hrs or old_end_hrs <= new_start_hrs): # проверка на конфликт дел по времени
                return HttpResponse('Ошибка. новое дело конфликтует со старым. потом перестилизуешь👍👍👍')
        day.objects.filter(id=case_id, user=user_tmp).update(case_start=start, case_end=end, case=case_name, case_description=description)

        return HttpResponseRedirect("/profile/"+day_short)