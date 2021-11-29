from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

from .models import ContactUs, Feedback

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'issue', 'issue_description', 'img', 'call']
    
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'like_comment', 'miss', 'email']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password':{
                'write_only':True,  #hide password on get request
                'required':True     #compulsory for user to input
            },
            'email':{
                'required':True,
            }
        }
        
    def create(self, validated_data):
        # Encrypting the password in database
        user = User.objects.create_user(**validated_data)
        # Create Token Automatically
        Token.objects.create(user=user)
        return user