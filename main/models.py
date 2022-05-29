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


class New(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()
    image = models.ImageField(upload_to='images')


# class HelpImage(models.Model):
#     image = models.ImageField(upload_to='images')


class About(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()


class AboutImage(models.Model):
    image = models.ImageField(upload_to='abouts', blank=True, null=True)
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')
