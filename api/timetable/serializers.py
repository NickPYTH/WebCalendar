from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Timetable

class TimetableSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    start_time = serializers.TimeField(required=True)
    end_time = serializers.TimeField(required=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        model = Timetable
        fields = (
            'user',
            'date',
            'start_time',
            'end_time',
            'name',
            'description'
        )

    def create(self, validated_data):
        record = Timetable.objects.create(
            user=User.objects.get(username=validated_data['user']),
            date=validated_data['date'],
            start_time=validated_data['start_time'],
            end_time=validated_data['end_time'],
            name=validated_data['name'],
            description=validated_data['description'],
        )

        return record
