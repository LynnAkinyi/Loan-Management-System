from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.caption



class FormData(models.Model):
    Last_Name = models.TextField(max_length=25)
    First_Name = models.TextField(max_length=25)
    Acount_Number = models.TextField(max_length=25, default='')
    Amount = models.IntegerField()

