from django.db.models import query
from django.shortcuts import render
from .models import ContactUs, Feedback
from .serializers import ContactUsSerializer, FeedbackSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [IsAuthenticated]          #check user have permission to access
    authentication_classes = (TokenAuthentication,) #check user token
    
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    