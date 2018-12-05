from django.db import models

# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')
