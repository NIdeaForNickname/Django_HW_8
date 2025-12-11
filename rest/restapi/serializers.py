from .models import Task
from rest_framework import serializers
from django.utils import timezone
import datetime

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    time_left = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ["name", "text", "deadline", "time_left"]
    
    def get_time_left(self, obj):
        return str(obj.deadline - timezone.now())

