from django.forms import ValidationError
from rest_framework import serializers
from .models import User, Logs
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, clean_data):
        print(clean_data)
        username = clean_data.get("username")
        password = clean_data.get("password")

        if username is None or password is None:
            raise serializers.ValidationError("Username and password are required")
        
        user = authenticate(username =username, password = password)

        if user is None:
            raise serializers.ValidationError('Invalid Username Or Password')
     
        clean_data['user'] = user
        return clean_data


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if User.objects.filter(username=value).exists(): #checks the database for existing username
            raise serializers.ValidationError("Username already exists")
        return value
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")

      
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one digit")

       
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter")

        
        if not any(char in "!@#$%^&*()_+-=" for char in value):
            raise serializers.ValidationError("Password must contain at least one special character")

        return value


    def create(self, clean_data):
        userOBJ = User.objects.create_user(username=clean_data['username'], password=clean_data['password'])
        userOBJ.save()
        return userOBJ