from django.db import models

# Create your models here.

class Emails(models.Model):
    user_email = models.EmailField(max_length=100, blank=False)
