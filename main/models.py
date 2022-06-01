from colorfield.fields import ColorField
from django.core.validators import RegexValidator
from django.db import models
from fontawesome_5.fields import IconField


"""Главная страница(Слайдер)"""


class Main(models.Model):
    image = models.ImageField(upload_to='image', blank=True, null=True)
    link = models.URLField(max_length=500, null=True)


"""Преимущества"""


class Advantages(models.Model):
    icon = models.FileField(null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()


"""Коллекция"""


class Collection(models.Model):
    image = models.ImageField(upload_to='collection_image', blank=True, null=True)
    name = models.CharField(max_length=220, unique=True, null=True)


"""Публичная оферта"""


class Public(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField()


"""Новости"""


class New(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()


"""Помощь"""


class Help(models.Model):
    question = models.TextField()
    answer = models.TextField()


class HelpImage(models.Model):
    image = models.ImageField(upload_to='images')


"""О нас"""


class About(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(blank=True, null=True)


class AboutImage(models.Model):
    image = models.ImageField(upload_to='abouts', blank=True, null=True)
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')


"""Футер"""


class Footer(models.Model):
    logo = IconField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)


"""Футер соц.сети"""


class FooterTwo(models.Model):
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, null=True, blank=True)
    telegram = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    email = models.URLField(max_length=500, blank=True, null=True)
    whatsapp = models.CharField(validators=[phoneNumberRegex], max_length=16, null=True, blank=True)


def save(self):
    self.whatsapp = 'https://wa.me/' + str(self.whatsapp)
    super(FooterTwo, self).save()


"""Товар"""


class Product(models.Model):
    collections = models.ForeignKey(Collection, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    vendorcode = models.TextField()
    price = models.IntegerField(null=True)
    # size = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=CHOOSE_SIZE)
    sale = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Скидка')
    new_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, verbose_name="Описание")
    material = models.CharField(max_length=200)
    structure = models.CharField(max_length=200)
    new = models.BooleanField(default=False, blank=True, null=True)
    hit = models.BooleanField(default=False, blank=True, null=True)
    favorite = models.BooleanField(default=False, blank=True, null=True)

    def save(self):
        if self.sale != 0:
            new = (self.price * self.sale) / 100
            self.new_price = self.price - new
            super(Product, self).save()
        else:
            super(Product, self).save()


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    color = ColorField()


"""Обратный звонок"""


class BackCall(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True, blank=True)
    data = models.DateTimeField()
    types = models.CharField(max_length=200)
    status = models.BooleanField(blank=True, null=True, default=False)
