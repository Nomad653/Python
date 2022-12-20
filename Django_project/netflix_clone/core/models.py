from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

AGE_CHOICES = (("All",'All'),("Kids","Kids"))

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile',null=True,blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.models.CharField(max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4)
    
class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1400)
    