from django.shortcuts import render

from .serializers import UserProfileSerializer, ProfileFeedItemSerializer
from .models import UserProfile, ProfileFeedItem
from .permissions import UpdateOwnProfile, UpdateOwnStatus

from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', 'email',)

class UserLoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ProfileFeedViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateOwnStatus, IsAuthenticatedOrReadOnly ]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)





