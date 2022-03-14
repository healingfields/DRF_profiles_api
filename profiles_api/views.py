from django.shortcuts import render

from .serializers import UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile

from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [UpdateOwnProfile]




