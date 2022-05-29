from django.db import models
from fontawesome_5.fields import IconField


class Main(models.Model):
    image = models.ImageField(upload_to='image')
    link = models.URLField(max_length=200)


class Advantages(models.Model):
    icon = IconField()
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()


class Collection(models.Model):
    image = models.ImageField(upload_to='collection_image')
    name = models.CharField(max_length=220, unique=True)


class Public(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()
