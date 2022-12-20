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
    description = models.TextField(blank=True,null=True,max_length=1400)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    