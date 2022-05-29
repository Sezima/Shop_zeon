from django.db import models

class Main(models.Model):
    image = models.ImageField(upload_to='image')
    link = models.URLField(max_length=200)
