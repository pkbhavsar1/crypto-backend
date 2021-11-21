from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Contact, Feedback

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','first_name', 'last_name', 'email_id', 'contact', 'issue_description']
    
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'like_comment', 'miss', 'email']