from django.db import models
import datetime
from django.utils import timezone


def return_date_time():
    now = timezone.now()
    return now

# Create your models here.
class Messages(models.Model):
    From = models.CharField(max_length = 13)
    To = models.CharField(max_length = 13)
    Text = models.CharField(max_length = 1024, blank = True)
    date_time = models.DateTimeField(default = return_date_time)
    photo = models.ImageField(upload_to = 'images', blank = True)

class PhotoBank(models.Model):
    photo = models.ImageField(upload_to = 'images', blank = True)
