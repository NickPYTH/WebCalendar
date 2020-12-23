from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse
from timetable.models import *
from timetable.views import calc_time


def main_page(request):
    try:
        #del request.session['user_name']
        User.objects.get(user_name=request.session['user_name'])
        data = {
        'user' : request.session['user_name'],  
        }
        return render(request, "index.html", data)
    except:
        data = {
            'user' : "None",
        }
        return render(request, "index.html", data)

def registration(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_mail = request.POST['mail']
        user_password = request.POST['password']

        try:
            User.objects.create(
                user_name=user_name,
                user_mail=user_mail,
                user_password=user_password
            )
        except: 
            data = {
                'username_exists': True,
                }
            return render(request, "registration/registration.html", data)
        
        user_tmp = User.objects.get(user_mail=user_mail)
        if user_tmp.user_password == request.POST['password']:
            request.session['user_name'] = user_tmp.user_name
        request.session['current_user'] = user_name
        for day in [Monday, Tuesday, Wednesday, Thursday, Friday]:
            day.objects.create(
                id=None,
                case_start="00:00:00",
                case_end="08:00:00",
                case="Dream", 
                case_description="Sweety dreams",
                user=user_tmp,
                is_default=True)
            day.objects.create(
                id=None,
                case_start="00:00:00",
                case_end="08:00:00",
                case="Dream", 
                case_description="Sweety dreams",
                user=user_tmp,
                is_default=False)
            day.objects.create(
                id=None,
                case_start="09:00:00",
                case_end="15:00:00",
                case="Job", 
                case_description="Fucking job..",
                user=user_tmp,
                is_default=False)
            day.objects.create(
                id=None,
                case_start="09:00:00",
                case_end="15:00:00",
                case="Job", 
                case_description="Fucking job..",
                user=user_tmp,
                is_default=True)
        for day in [Saturday, Sunday]:
            day.objects.create(
                id=None,
                case_start="00:00:00",
                case_end="10:00:00",
                case="Dream", 
                case_description="Sweety dreams",
                user=user_tmp,
                is_default=True)
            day.objects.create(
                id=None,
                case_start="00:00:00",
                case_end="10:00:00",
                case="Dream", 
                case_description="Sweety dreams",
                user=user_tmp,
                is_default=False)
            
        
        return render(request, "registration/success_registration.html")
    else:
        return render(request, "registration/registration.html")

def logout(request):
    try:
        del request.session['user_name']
    except:
        pass
    return render(request, "registration/logout.html")

def login(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_password = request.POST['password']

        try:
            User.objects.get(
                user_name=user_name,
            )
        except: 
            data = {    
                'doest_exist': True,
                'password_incorrect' : False,
                }
            return render(request, "registration/login.html", data)

        try:
            User.objects.get(
                user_name=user_name,
                user_password=user_password
            )
        except: 
            data = {    
                'doest_exist': False,
                'password_incorrect' : True,
                }
            return render(request, "registration/login.html", data)

        user_tmp = User.objects.get(user_name=user_name)
        if user_tmp.user_password == request.POST['password']:
            request.session['user_name'] = user_tmp.user_name

        monday_data = Monday.objects.filter(user=user_tmp.id)
        
        cases_tmp = [case for case in monday_data]
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
        monday_data = []
        busy_time = 0
        free_time = 24
        for case in cases_sorted_by_time:
            tmp = []
            tmp.append(case.case)  # Задача
            tmp.append(case.case_description)  # Описание задачи
            tmp.append(calc_time(case.case_start, case.case_end))  # Длительность
            tmp.append(case.case_start.hour)  # начало
            tmp.append(case.case_end.hour)  # конец
            monday_data.append(tmp)
            busy_time += calc_time(case.case_start, case.case_end)
        
        progress_bar = int((busy_time/24)*100)


        data = {    
                'day' : 'Monday',
                'busy_time' : busy_time,
                'empty_time' : free_time - busy_time,
                'cases' : monday_data,
                'progress' : progress_bar,
                }
                
        return render(request, "webcalendar/profile.html", data)

    else:
        data = {
                'doest_exist': False,
                'password_incorrect' : False,
                }
        return render(request, "registration/login.html", data)
