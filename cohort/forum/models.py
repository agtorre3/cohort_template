from django.contrib.auth.models import User
from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
# Create your models here.
