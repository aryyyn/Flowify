from django.urls import path
from .views import Register,Login, UserView,Logout

urlpatterns = [
    path('register', view=Register.as_view()), 
    path('login', view=Login.as_view()),
    path('logout', view=Logout.as_view()), #sends a request to the frontend to remove the sessionID from the browser
    path('user', view=UserView.as_view()),  #API for logged users (to view their information)

]
