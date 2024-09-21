from logging import raiseExceptions
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegisterSerializer, LoginSerializer, UserSerializer
import jwt, datetime
from .models import User



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
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data.get('user')
        
            payload = {
                'id': user.id,
                'expiration': (datetime.datetime.utcnow() + datetime.timedelta(minutes=60)).isoformat(),  # Token will expire in 60 minutes
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm="HS256")

            
            

            response =  Response(
                {
                    'message': 'Info is correct!',
                    'data': {'user_id': user.id, 'username': user.username, 'jwt': token}
                }, status=status.HTTP_200_OK
            )
            response.set_cookie(key="jwt", value=token, httponly=True)
            return response
        else:
            return Response(
                {
                    'message': "Login Failed",
                    'data': serializer.errors
                }, status=status.HTTP_401_UNAUTHORIZED
            )


class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response ( 
                {
                    'message': "Failed",
                    'data': "Not authenticated"
                }, status=status.HTTP_401_UNAUTHORIZED
            )
        
        else:
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])

            except jwt.ExpiredSignatureError:
                return Response ( 
                {
                    'message': "Failed",
                    'data': "Not authenticated"
                }, status=status.HTTP_401_UNAUTHORIZED
            )

            user = User.objects.filter(user_id = payload['id']).first()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        

class Logout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
            
        