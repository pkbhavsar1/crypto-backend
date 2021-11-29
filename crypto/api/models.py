from typing import Sized
from django.db import models

class ContactUs(models.Model):
    issue = models.CharField(max_length=100, null=False)
    issue_description = models.TextField(null=False)
    img = models.TextField()
    call = models.CharField(max_length=5)

class Feedback(models.Model):
    like_comment = models.TextField(null=True)
    miss = models.TextField(null=True)
    email = models.EmailField(max_length=254, null=False)
    