from rest_framework import serializers
from sportsForecastBackend.models import models

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields = '__all__'