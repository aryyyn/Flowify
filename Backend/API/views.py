from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegisterSerializer, LoginSerializer




class Register(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response({
                'message': 'User registered successfully!',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        else:
             return Response(
                 {
                     'message': "Registration Failed",
                     'data': serializer.errors
                 }, status=status.HTTP_403_FORBIDDEN
             )
        
        
class Login(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        # print(request.data)
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get('user')
           
            return Response(
                {
                    'message': 'Info is correct!',
                    'data': {'user_id': user.id, 'username': user.username}
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    'message': "Login Failed",
                    'data': serializer.errors

                }, status=status.HTTP_401_UNAUTHORIZED
            )