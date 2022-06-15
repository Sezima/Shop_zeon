from rest_framework import serializers
from .models import *


class CollectionSerializer(serializers.ModelSerializer):
    """Коллекция"""

    class Meta:
        model = Collection
        fields = '__all__'


class PublicSerializer(serializers.ModelSerializer):
    """Публичная оферта"""

    class Meta:
        model = Public
        fields = ('title', 'text')


class NewSerializer(serializers.ModelSerializer):
    """Новости"""

    class Meta:
        model = New
        fields = ('image', 'title', 'text')


class HelpSerializer(serializers.ModelSerializer):
    """Помощь"""

    class Meta:
        model = Help
        fields = ('question', 'answer')


class HelpImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpImage
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    """О нас"""

    class Meta:
        model = About
        fields = ('title', 'text')


class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    """Товар"""

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

    # не проверен
    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = self._get_image_url(instance)
        return representation


class FooterSerializer(serializers.ModelSerializer):
    """Футер"""

    class Meta:
        model = Footer
        fields = ('logo', 'text', 'number')


class FooterTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterTwo
        fields = ('number', 'telegram', 'instagram', 'email', 'whatsapp')


class NewProductSerializer(serializers.ModelSerializer):
    """Новинки"""

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'new_price', 'sale', 'favorites', 'new', 'hit', 'size')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation


class HitProductSerializer(serializers.ModelSerializer):
    """Хит продаж"""

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'new_price', 'sale', 'favorites', 'new', 'hit', 'size')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation


class MainSerializer(serializers.ModelSerializer):
    """Главная страница"""

    class Meta:
        model = Main
        fields = ('image', 'link')


class AdvantagesSerializer(serializers.ModelSerializer):
    """Преимущества"""

    class Meta:
        model = Advantages
        fields = ('icon', 'title', 'text')


class FavoritesSerializer(serializers.ModelSerializer):
    """Избранные"""

    class Meta:
        model = Favorites
        fields = '__all__'

    def create(self, validated_data):
        fav = validated_data.get('fav')
        favorite = Favorites.objects.get_or_create(fav=fav)[0]
        favorite.favorites = True if favorite.favorites is False else False
        favorite.save()
        if favorite.favorites == True:
            favorite.save()
        else:
            favorite.delete()

        return favorite

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.fav.images.all(), many=True).data
        representation['name'] = instance.fav.title
        representation['price'] = instance.fav.price
        representation['size'] = instance.fav.size
        representation['new_price'] = instance.fav.new_price
        return representation


class DetailSerializer(serializers.ModelSerializer):
    """товары этой коллекции"""

    class Meta:
        model = Collection
        fields = ('id',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product.all(), many=True).data
        return representation


class BackCallSerializer(serializers.ModelSerializer):
    """Обратный звонок"""

    class Meta:
        model = BackCall
        fields = ('name', 'number', 'types')


class UserSerializer(serializers.ModelSerializer):
    """Информация юзера"""

    class Meta:
        model = User
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('quantity', 'order')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.product.cart.images.all(), many=True).data
        representation['name'] = instance.product.cart.title
        representation['price'] = instance.product.cart.price
        representation['size'] = instance.product.cart.size
        representation['new_price'] = instance.product.cart.new_price
        return representation



class CaseSerializer(serializers.ModelSerializer):
    """корзина"""

    class Meta:
        model = Case
        fields = ('id', 'quantity', )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.cart.images.all(), many=True).data
        representation['name'] = instance.cart.title
        representation['price'] = instance.cart.price
        representation['size'] = instance.cart.size
        representation['new_price'] = instance.cart.new_price

        return representation




class CartSerializer(serializers.ModelSerializer): #инфо о заказе
    class Meta:
        model = Order
        fields = ('get_count', )













