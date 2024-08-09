from django.db import models

# Create your models here.

class AllUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
