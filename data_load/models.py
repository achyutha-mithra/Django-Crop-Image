from django.db import models
from django.db.models.query import QuerySet
from django_group_by import GroupByMixin


class Image_Upload(models.Model):
    array = models.CharField(max_length=300)

    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='pics/')
