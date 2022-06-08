from itertools import count

from colorfield.fields import ColorField
from django.core.validators import RegexValidator
from django.db import models
from fontawesome_5.fields import IconField

from zeon import settings

"""Главная страница(Слайдер)"""


class Main(models.Model):
    image = models.ImageField(upload_to='image', verbose_name="Фотография")
    link = models.URLField(max_length=500, blank=True, verbose_name="Ссылка")

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


"""Преимущества"""


class Advantages(models.Model):
    icon = models.FileField(verbose_name="Иконка")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'


"""Коллекция"""


class Collection(models.Model):
    image = models.ImageField(upload_to='collection_image', verbose_name="Фотография")
    name = models.CharField(max_length=220, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекция'


"""Публичная оферта"""


class Public(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'


"""Новости"""


class New(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="Фотография")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


"""Помощь"""


class Help(models.Model):
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощь'


class HelpImage(models.Model):
    image = models.ImageField(upload_to='images', verbose_name="Фотография")

    class Meta:
        verbose_name = 'Помощь фото'
        verbose_name_plural = 'Помощь фото'


"""О нас"""


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class AboutImage(models.Model):
    image = models.ImageField(upload_to='abouts', verbose_name="Фотография")
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')


"""Футер"""


class Footer(models.Model):
    logo = IconField(verbose_name="Логотип")
    text = models.TextField(verbose_name="Текстовая информация")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, verbose_name="Номер хедера")

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'


"""Футер соц.сети"""


class FooterTwo(models.Model):
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, null=True, blank=True)
    telegram = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    email = models.URLField(max_length=500, blank=True, null=True)
    whatsapp = models.CharField(null=True, blank=True, max_length=250)

    def save(self):
        if self.whatsapp.isdigit() or self.whatsapp.startswith('+'):
            self.whatsapp = 'https://wa.me/' + str(self.whatsapp)
            super(FooterTwo, self).save()
        else:
            super(FooterTwo, self).save()

    class Meta:
        verbose_name = 'Футер соц.сети'
        verbose_name_plural = 'Футер соц.сети'


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
    price = models.IntegerField(verbose_name="Цена", default=0)
    size = models.CharField(max_length=20, default='42-50', verbose_name="Размер")
    amount = models.IntegerField(default=5, verbose_name="Количество в линейке")
    sale = models.IntegerField(default=0, blank=True, verbose_name='Скидка')
    new_price = models.IntegerField(blank=True, default=0, verbose_name="Новая цена")
    description = models.TextField(verbose_name="Описание")
    material = models.CharField(max_length=200, verbose_name="Материал")
    structure = models.CharField(max_length=200, verbose_name="Состав ткани")
    new = models.BooleanField(verbose_name="Новинки")
    hit = models.BooleanField(verbose_name="Хит продаж")
    favorites = models.BooleanField(verbose_name="Избранные")
    
    def save(self):
        if self.new_price != 0:
            self.sale = self.price - self.new_price
            super(Product, self).save()
        else:
            super(Product, self).save()

    # def save(self):
    #     if self.sale != 0:
    #         new = (self.price * self.sale) / 100
    #         self.new_price = self.price - new
    #         super(Product, self).save()
    #     else:
    #         super(Product, self).save()

    

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name="Фотография")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    color = ColorField()


"""Обратный звонок"""


class BackCall(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Имя")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True,
                              null=True, blank=True, verbose_name="Номер телефона")
    data = models.DateTimeField(verbose_name="Дата обращения")
    types = models.CharField(max_length=200, verbose_name="Тип обращения", default='Обратный звонок')
    status = models.BooleanField(blank=True, null=True, default=False, verbose_name="Статус")

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратный звонок'


"""заказ инфо о юзере"""

STATUS = (
    ('new', 'новый'),
    ('order', 'оформлен'),
    ('cancel', 'отмена')
)


class User(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, verbose_name="Номер телефона")
    country = models.CharField(max_length=150, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    date = models.DateField(verbose_name='Дата оформления')
    status = models.CharField(max_length=100, choices=STATUS, default='new', verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'


"""Заказ"""


class Order(models.Model):
    order = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)


    def get_count(self):
        c = 0
        cost = 0
        sale = 0
        endCost = 0
        for i in Order.objects.all():
            c += i.quantity
            p = c * 5
            cost += i.quantity * i.product.price
            endCost = cost - sale

            if i.product.new_price != 0:
                sale += (i.product.price - i.product.new_price) * i.quantity
            else:
                continue


        return f'Колличество линейки {c}, ' \
               f'колличество товаров {p}, ' \
               f'Стоимость {cost}, ' \
               f'Скидка {sale}, ' \
               f'Итог {endCost}, '


"""Корзина"""


class Case(models.Model):
    cases = models.BooleanField(default=False)
    cart = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cases')
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.cases)



    def get_count(self):
        c = 0
        cost = 0
        sale = 0
        endCost = 0
        for i in Case.objects.all():
            c += i.quantity
            p = c * 5
            cost += i.quantity * i.cart.price
            endCost = cost - sale

            if i.cart.new_price != 0:
                sale += (i.cart.price - i.cart.new_price) * i.quantity
            else:
                continue


        return f'Колличество линейки {c}, ' \
               f'колличество товаров {p}, ' \
               f'Стоимость {cost}, ' \
               f'Скидка {sale}, ' \
               f'Итог {endCost}, '
