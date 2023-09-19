from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializers


class Userview(APIView):
    def get(self,request):
        serializer=UserSerializers(request.user)
        return Response(serializer.data)
