"""webcalendar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from timetable import views as cal_views
from registration import views as reg_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', reg_views.main_page, name="index"),
    path('registration/', reg_views.registration, name="registration"),
    path('login/', reg_views.login, name="login"),
    path('profile/', cal_views.profile, name="profile"),

    path('profile/mnd', cal_views.monday, name="monday"),
    path('profile/tue', cal_views.tuesday, name="tuesday"),
    path('profile/wed', cal_views.wednesday, name="wednesday"),
    path('profile/thu', cal_views.thursday, name="thursday"),
    path('profile/fri', cal_views.friday, name="friday"),
    path('profile/sat', cal_views.saturday, name="saturday"),
    path('profile/sun', cal_views.sunday, name="sunday"),
]
