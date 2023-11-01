from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='project img')
    desc=models.TextField()

    def __str__(self):
        return self.name

class people(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='project img')


    def __str__(self):
        return self.name
