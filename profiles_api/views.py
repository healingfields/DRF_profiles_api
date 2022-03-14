from django.shortcuts import render

from .serializers import UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile

from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'email',)

class UserLoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES




