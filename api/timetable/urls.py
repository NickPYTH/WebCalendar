from django.urls import path
from .views import CreateTimetableView, GetAllUserTimetablesList, UpdateUserTimetableView


urlpatterns = [
    path('create_user_task/', CreateTimetableView.as_view(), name='create_user_task'),
    path('get_all_user_tasks/', GetAllUserTimetablesList.as_view(), name='get_all_user_tasks'),
    path('update_user_task/', UpdateUserTimetableView.as_view(), name='update_user_tasks'),

]