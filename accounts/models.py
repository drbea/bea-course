from django.db import models

# Create your models here.
    

class UserModel(models.Model):
    name = models.CharField( max_length=50)
    username = models.CharField(max_length = 70)
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=50)
    