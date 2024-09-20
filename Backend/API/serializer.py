from rest_framework import serializers
from .models import User, Logs

class UserSerializer(serializers.ModelSerializer)