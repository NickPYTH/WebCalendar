from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from .serializers import TimetableSerializer
from .models import Timetable

class CreateTimetableRecordView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TimetableSerializer

class GetAllUserTimetablesRecorsList(generics.ListCreateAPIView):
    queryset = Timetable.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TimetableSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TimetableSerializer(queryset.all(), many=True)
        return Response(serializer.data)

class UpdateUserTimetableView(generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TimetableSerializer