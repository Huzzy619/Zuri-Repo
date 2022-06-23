from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


# Return the User model that is active in this project.
User = get_user_model()

class Post (models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now= True)
    published_date = models.DateTimeField(default = timezone.now)
