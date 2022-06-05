from colorfield.fields import ColorField
from django.core.validators import RegexValidator
from django.db import models
from fontawesome_5.fields import IconField

"""Главная страница(Слайдер)"""


class Main(models.Model):
    image = models.ImageField(upload_to='image', verbose_name="Фотография")
    link = models.URLField(max_length=500, verbose_name="Ссылка")


"""Преимущества"""


class Advantages(models.Model):
    icon = models.FileField( verbose_name="Иконка")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")


"""Коллекция"""


class Collection(models.Model):
    image = models.ImageField(upload_to='collection_image', verbose_name="Фотография")
    name = models.CharField(max_length=220, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name


"""Публичная оферта"""


class Public(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")


"""Новости"""


class New(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="Фотография")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")


"""Помощь"""


class Help(models.Model):
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")


class HelpImage(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="Фотография")


"""О нас"""


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(blank=True, verbose_name="Описание")


class AboutImage(models.Model):
    image = models.ImageField(upload_to='abouts', verbose_name="Фотография")
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')


"""Футер"""


class Footer(models.Model):
    logo = IconField(verbose_name="Логотип")
    text = models.TextField(verbose_name="Текстовая информация")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, verbose_name="Номер хедера")


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


# CHOOSE_SIZE = [
#     ('40', '40'),
#     ('42', '42'),
#     ('44', '44'),
#     ('46', '46'),
#     ('48', '48')
#
# ]


class Product(models.Model):
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='product')

    title = models.CharField(max_length=150, verbose_name="Название товара")
    vendorcode = models.TextField(verbose_name="Артикул товара")
    price = models.IntegerField(verbose_name="Цена")
    # size = models.CharField(max_length=5, choices=CHOOSE_SIZE)
    size = models.CharField(max_length=20, blank=True, null=True, default='42-50', verbose_name="Размер")
    amount = models.IntegerField(default=5, verbose_name="Количество в линейке")
    sale = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, verbose_name='Скидка')
    new_price = models.IntegerField(blank=True, null=True, verbose_name="Новая цена")
    description = models.TextField(blank=True, verbose_name="Описание")
    material = models.CharField(max_length=200, verbose_name="Материал")
    structure = models.CharField(max_length=200, verbose_name="Состав ткани")
    new = models.BooleanField(default=False, blank=True, null=True, verbose_name="Новинки")
    hit = models.BooleanField(default=False, blank=True, null=True, verbose_name="Хит продаж")
    # like = models.BooleanField(default=False, blank=True, null=True)

    def save(self):
        if self.sale != 0:
            new = (self.price * self.sale) / 100
            self.new_price = self.price - new
            super(Product, self).save()
        else:
            super(Product, self).save()


    def __str__(self):
        return f'{self.title}'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name="Фотография")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    color = ColorField()


"""Обратный звонок"""


class BackCall(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Имя")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True, blank=True, verbose_name="Номер телефона")
    data = models.DateTimeField(verbose_name="Дата обращения")
    types = models.CharField(max_length=200, verbose_name="Тип обращения", default='Обратный звонок')
    status = models.BooleanField(blank=True, null=True, default=False, verbose_name="Статус")


class Favorite(models.Model):
    favorites = models.BooleanField(default=False)
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return str(self.favorites)
