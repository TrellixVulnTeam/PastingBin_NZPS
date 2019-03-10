from django.db import models
from django.urls import reverse
import datetime
import uuid

# Create your models here.
from django.contrib.auth.models import User, AbstractUser # Required to assign User as a creator of a post

class user(AbstractUser):
    email = models.EmailField(max_length=254, help_text='Required. Input a valid email address.')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class PostTable(models.Model):
    postID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this post")
    expiry = models.DateField(default=datetime.date.today)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    private = models.BooleanField(default=0)
    pasteContent = models.CharField(max_length=2000)


    def __str__(self):
        return self.pasteContent
