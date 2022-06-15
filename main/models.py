from colorfield.fields import ColorField
from django.core.validators import RegexValidator
from django.db import models

from main.validator import validate_file


class Main(models.Model):
    """Главная страница(Слайдер)"""
    image = models.ImageField(upload_to='image', verbose_name="Фотография")
    link = models.URLField(max_length=500, blank=True, verbose_name="Ссылка")

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class Advantages(models.Model):
    """Преимущества"""
    icon = models.ImageField(verbose_name="Иконка", validators=[validate_file])
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Наши преимущества'
        verbose_name_plural = 'Наши преимущества'


class Collection(models.Model):
    """Коллекция"""
    image = models.ImageField(upload_to='collection_image', verbose_name="Фотография")
    name = models.CharField(max_length=220, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекция'


class Public(models.Model):
    """Публичная оферта"""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'


class New(models.Model):
    """Новости"""
    image = models.ImageField(upload_to='images', verbose_name="Фотография")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Help(models.Model):
    """Помощь"""
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


class About(models.Model):
    """О нас"""
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class AboutImage(models.Model):
    image = models.ImageField(upload_to='abouts', verbose_name="Фотография")
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images')


class BackCall(models.Model):
    """Обратный звонок"""
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


class Footer(models.Model):
    """Футер"""
    logo = models.ImageField(upload_to='image', verbose_name="Фотография", validators=[validate_file])  # do FileField
    text = models.TextField(verbose_name="Текстовая информация")
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, verbose_name="Номер хедера")

    class Meta:
        verbose_name = 'Футер'
        verbose_name_plural = 'Футер'


class FooterTwo(models.Model):
    """Футер соц.сети"""
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


class Product(models.Model):
    """Товар"""
    collections = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='product')

    title = models.CharField(max_length=150, verbose_name="Название товара")
    vendorcode = models.TextField(verbose_name="Артикул товара")
    price = models.IntegerField(verbose_name="Цена", default=0)
    size = models.CharField(max_length=20, default='42-50', verbose_name="Размер")
    amount = models.IntegerField(default=5, verbose_name="Количество в линейке", blank=True)
    sale = models.IntegerField(default=0, blank=True, verbose_name='Скидка')
    new_price = models.IntegerField(blank=True, default=0, verbose_name="Новая цена")
    description = models.TextField(verbose_name="Описание")
    material = models.CharField(max_length=200, verbose_name="Материал")
    structure = models.CharField(max_length=200, verbose_name="Состав ткани")
    new = models.BooleanField(verbose_name="Новинки")
    hit = models.BooleanField(verbose_name="Хит продаж")

    def save(self):
        if self.new_price != 0:
            self.sale = self.price - self.new_price
            super(Product, self).save()
        else:
            super(Product, self).save()

    def save(self):
        n = ((int(self.size[3:]) - int(self.size[:2])) // 2) + 1
        self.amount = n
        super(Product, self).save()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name="Фотография")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    color = ColorField()





class Favorites(models.Model):
    favorites = models.BooleanField(default=False)
    fav = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return str(self.favorites)


"""Заказ , корзина и инфо"""

STATUS = (
    ('new', 'новый'),
    ('order', 'оформлен'),
    ('cancel', 'отмена')
)
class User(models.Model):
    """Инфо о юзере"""
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
        verbose_name = 'Заказщик'
        verbose_name_plural = 'Заказшик'

    def __str__(self):
        return self.name


"""Корзина"""



class Case(models.Model):
    cart = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cases')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Колличество товара')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'{self.cart}'

    # удаление продукта
    # def del_product(self):
    #     if (self.cart == Order.product) and User.status == 'order':
    #         self.cart.delete()
    #     else:
    #         self.cart.save()



"""Заказ"""


class Order(models.Model):
    order = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    product = models.ForeignKey(Case, related_name='product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{}'.format(self.id)





    def get_count(self):
        c = 0
        cost = 0
        sale = 0
        endCost = 0
        for i in Order.objects.all():
            c += i.quantity
            p = c * i.product.cart.amount
            cost += i.quantity * i.product.cart.price
            endCost = cost - sale

            if i.product.cart.new_price != 0:
                sale += (i.product.cart.price - i.product.cart.new_price) * i.quantity
            else:
                continue

        return f'Колличество линейки {c}, ' \
               f'колличество товаров {p}, ' \
               f'Стоимость {cost}, ' \
               f'Скидка {sale}, ' \
               f'Итог {endCost}, '
