from rest_framework import serializers
from .models import JobAd, JobApplication

class JobAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAd
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'
