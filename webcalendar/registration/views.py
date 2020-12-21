from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import User
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse
from timetable.models import *


def main_page(request):
    data = {
        
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
            request.session['user_id'] = user_tmp.id
        request.session['current_user'] = user_name
        monday_tmp = Monday(
            id=None,
            case_start="23:00:00",
            case_end="07:00:00",
            case="Dream", 
            case_description="Sweety dreams",
            user=user_tmp)
        monday_tmp.save()
        return render(request, "registration/success_registration.html")
    else:
        return render(request, "registration/registration.html")

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
            request.session['user_id'] = user_tmp.id

        monday_tmp = Monday(
            id=None,
            case_start="11:00:00",
            case_end="07:00:00",
            case="Dream", 
            case_description="Sweety dreams",
            user=user_tmp)
        monday_tmp.save()

        monday_data = Monday.objects.filter(user=user_tmp.id)

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
                'busy_time' : 16,
                'empty_time' : 84,
                }
        
        return render(request, "webcalendar/profile.html", data)

    else:
        data = {
                'doest_exist': False,
                'password_incorrect' : False,
                }
        return render(request, "registration/login.html", data)
