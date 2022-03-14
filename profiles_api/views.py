from django.shortcuts import render

from .serializers import UserProfileSerializer
from .models import UserProfile

from rest_framework import viewsets
from rest_framework import status

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()




