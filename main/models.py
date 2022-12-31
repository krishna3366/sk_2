from django.db import models

# Create your models here.

class Enquiry(models.Model):
    hospital = models.CharField(max_length=200,null=True)
    branch = models.CharField(max_length=200)
    country = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    supervisor = models.CharField(max_length=200)
    email = models.EmailField(null=True)

class Feedback(models.Model):
    email=models.EmailField()
    feedback=models.TextField()