from django.db import models

# Create your models here.
class AppAuth(models.Model):
    access_token = models.CharField(max_length=255)  # Adjust the max_length based on your token length
    refresh_token = models.CharField(max_length=255)
    expiration_time = models.DateTimeField()
