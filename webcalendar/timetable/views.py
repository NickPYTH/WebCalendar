from django.shortcuts import render
from .models import *
from registration.models import *
from datetime import datetime, time, timedelta

def calc_time(start, end):
    end = timedelta(hours=end.hour, minutes=end.minute)
    start = timedelta(hours=start.hour, minutes=start.minute)
    return int((end - start).seconds / 3600)

def profile(request):
    user_tmp = User.objects.get(user_name=request.session['current_user'])

    monday_data = Monday.objects.filter(user=user_tmp.id)

    cases = []
    free_time = 24
    busy_time = 0
    progress_bar = 0

    for case in monday_data:
        cases.append(case)
        case_duration = free_time - calc_time(case.case_end, case.case_start)
        busy_time += case_duration
        free_time -= case_duration
        
    progress_bar = int((busy_time/24)*100)

    data = {    
                'day' : 'Monday',
                'doest_exist': False,
                'password_incorrect' : False,
                'monday_data' : Monday.objects.filter(user=user_tmp.id),
                'tuesday_data' : Tuesday.objects.filter(user=user_tmp.id),
                'wednesday_data' : Wednesday.objects.filter(user=user_tmp.id),
                'thursday_data' : Thursday.objects.filter(user=user_tmp.id),
                'friday_data' : Friday.objects.filter(user=user_tmp.id),
                'saturday_data' : Saturday.objects.filter(user=user_tmp.id),
                'sunday_data' : Sunday.objects.filter(user=user_tmp.id),
                'busy_time' : busy_time,
                'empty_time' : free_time,
                'name' : user_tmp.user_name,
                'cases' : cases,
                'progress' : progress_bar
            }     

    return render(request, "webcalendar/profile.html", context=data)