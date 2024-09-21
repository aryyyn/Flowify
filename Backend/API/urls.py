from django.urls import path
from .views import Register,Login

urlpatterns = [
    path('register', view=Register.as_view()), 
    path('login', view=Login.as_view()),
    # path('logout'), #sends a request to the frontend to remove the sessionID from the browser
    # path('user'),  #API for logged users (to view their information)

]
