from django.urls import path
from .views import CreateTimetableRecordView, GetAllUserTimetablesRecorsList, UpdateUserTimetableView, remove_task


urlpatterns = [
    path('create_user_task/', CreateTimetableRecordView.as_view(), name='create_user_task'),
    path('get_all_user_tasks/', GetAllUserTimetablesRecorsList.as_view(), name='get_all_user_tasks'),
    path('update_user_task/', UpdateUserTimetableView.as_view(), name='update_user_tasks'),
    path('remove_user_task/', remove_task, name='remove_task')
]
