from django.db import models

# Create your models here.

class soap(models.Model):
    sname =  models.CharField(max_length=30)
    sprice = models.IntegerField()
    sdes = models.CharField(max_length=100)

class paste(models.Model):
    sname =  models.CharField(max_length=30)
    sprice = models.IntegerField()
    sdes = models.CharField(max_length=100)
