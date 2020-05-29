from django.db import models
from django.contrib.auth.models import User

class Enquiry(models.Model):
    email = models.CharField(max_length=70)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True) # this will only update during craetion, not futher updatable

class Events(models.Model):
    event_name = models.CharField(max_length=200)
    event_code = models.CharField(max_length=20)
    referal_code = models.CharField(max_length=20)
    # hosted_by = models.CharField(max_length=100)
    hosted_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    event_description = models.TextField()
    event_status = models.IntegerField(default=0)
    # winner = models.CharField(max_length=100)
    starting_date = models.DateTimeField(default=None)
    ending_date = models.DateTimeField(default=None)

class Options(models.Model):
    option_name = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    event_code = models.ForeignKey(Events, on_delete=models.CASCADE)

# class Transactions(models.Model):
    # connect with user objcet (models.ForeignKey()) one to many relationship
    # time
    # option selected 
    # event_code
    # referal_code

