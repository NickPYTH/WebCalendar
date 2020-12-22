from django.shortcuts import render
from .models import *
from registration.models import *
from datetime import datetime, time, timedelta

def calc_time(start, end):
    end = timedelta(hours=end.hour, minutes=end.minute)
    start = timedelta(hours=start.hour, minutes=start.minute)
    return int((end - start).seconds / 3600)

def data_generation(request, data, day):
    cases_tmp = [case for case in data]
    cases_sorted_by_time = []
        
    while len(cases_tmp) != 0:
        min_ = 0
        for case in cases_tmp:
            if case.case_start.hour < min_ or min_ == 0:
                min_ = case.case_start.hour
                to_del = case
        cases_sorted_by_time.append(to_del)
        try:
            cases_tmp.remove(to_del)
        except:
            pass
    day_data = []
    busy_time = 0
    free_time = 24
    for case in cases_sorted_by_time:
        tmp = []
        tmp.append(case.case)  # Задача
        tmp.append(case.case_description)  # Описание задачи
        tmp.append(calc_time(case.case_start, case.case_end))  # Длительность
        tmp.append(case.case_start.hour)  # начало
        tmp.append(case.case_end.hour)  # конец
        day_data.append(tmp)
        busy_time += calc_time(case.case_start, case.case_end)
    progress_bar = int((busy_time/24)*100)

    return {
        'day' : day,
        "cases" : day_data,
        "busy_time" : busy_time,
        "empty_time" : free_time-busy_time,
        "progress": progress_bar,
        "user" : request.session['user_name'],
    }

def profile(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    monday_data = Monday.objects.filter(user=user_tmp.id)
    return render(request, "webcalendar/profile.html", context=data_generation(request,monday_data, 'Monday'))

def monday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Monday.objects.filter(user=user_tmp.id)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Monday'))

def tuesday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Tuesday.objects.filter(user=user_tmp.id)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Tuesday'))

def wednesday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Wednesday.objects.filter(user=user_tmp.id)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Wednesday'))

def thursday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Thursday.objects.filter(user=user_tmp.id)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Thursday'))

def friday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Friday.objects.filter(user=user_tmp.id)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Friday'))

def saturday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Saturday.objects.filter(user=user_tmp.id)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Saturday'))

def sunday(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])
    data = Sunday.objects.filter(user=user_tmp.id)
    return render(request, "webcalendar/profile.html", context=data_generation(request,data, 'Sunday'))