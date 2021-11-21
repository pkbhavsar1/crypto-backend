from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=254)
    contact = models.CharField(max_length=10, blank=False, null=False)
    issue_description = models.TextField(null=False, blank=False)
    
    
    def __str__(self):
        return self.first_name

class Feedback(models.Model):
    like_comment = models.TextField(null=True)
    miss = models.TextField(null=True)
    email = models.EmailField(max_length=254, null=False)
    