from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from user.views import Userview

urlpatterns = [

    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/me', Userview.as_view()),

]
