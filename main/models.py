from colorfield.fields import ColorField
from django import forms
from django.core.validators import RegexValidator
from django.db import models
from fontawesome_5.fields import IconField
from rest_framework.fields import FileField


class Main(models.Model):
    image = models.ImageField(upload_to='image', blank=True, null=True)
    link = models.URLField(max_length=500, null=True)


class Advantages(models.Model):
    icon = IconField()
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()


class Collection(models.Model):
    image = models.ImageField(upload_to='collection_image', blank=True, null=True)
    name = models.CharField(max_length=220, unique=True, null=True)


class Public(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()


class New(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()


class HelpImage(models.Model):
    image = models.ImageField(upload_to='images')


class About(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)


class AboutImage(models.Model):
    image = models.ImageField(upload_to='abouts', blank=True, null=True)
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')


class Footer(models.Model):
    logo = IconField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)


class FooterTwo(models.Model):
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=True)
    mail = models.URLField(blank=True)
    insta = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    whatsapp = models.URLField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=True)


class FooterTwoNumbers(models.Model):
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumbers = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, blank=True)
    footers = models.ForeignKey(FooterTwo, on_delete=models.CASCADE, related_name='phoneNumbers')


CHOOSE_SIZE = [
    ('42', '42'),
    ('44', '44'),
    ('46', '46'),
    ('48', '48'),
    ('50', '50'),
]
COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
        ("#ff0000", 'red'),
        ("#fd7715", 'orenge'),
        ("#fde415", 'yellow'),
        ("#3ff515", 'green'),
        ("#3fd1ff", 'blue'),
        ("#2c1fff", 'darkblue'),
        ("#3e2661", 'purple'),
]


class Product(models.Model):
    collections = models.ForeignKey(Collection, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    vendorcode = models.TextField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    size = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=CHOOSE_SIZE)
    sale = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Скидка')
    description = models.TextField(blank=True, verbose_name="Описание")
    material = models.CharField(max_length=200)
    structure = models.CharField(max_length=200)
    new = models.BooleanField(default=False)
    hit = models.BooleanField(default=False)

    def get_sale(self):
        prise = int((self.old_price * (100 - self.sale) / 100))
        return prise


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    color = ColorField()
