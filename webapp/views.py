from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import UserSerializer
from rest_framework import viewsets
from . models import Users

class UserData(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self):
        pass

    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    