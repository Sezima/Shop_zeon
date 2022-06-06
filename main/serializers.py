from requests import Response
from rest_framework import serializers

from .models import *

"""Коллекция"""


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


"""Публичная оферта"""


class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = ('title', 'text')


"""Новости"""


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('image', 'title', 'text')


"""Помощь"""


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('question', 'answer')


class HelpImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpImage
        fields = '__all__'


"""О нас"""


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title',  'text')


class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = '__all__'


"""Товар"""


class ProductSerializer(serializers.ModelSerializer):
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


"""Футер"""


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ('logo', 'text', 'number')


class FooterTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterTwo
        fields = ('number', 'telegram', 'instagram', 'email', 'whatsapp')


"""Коллекция(товара)"""


class CollProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product.all(), many=True).data
        return representation



"""Новинки"""


class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'new_price', 'sale', 'favorites', 'new', 'hit', 'size')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation


"""Хит продаж"""


class HitProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'new_price', 'sale', 'favorites', 'new', 'hit', 'size')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation


"""Главная страница"""


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ('image', 'link')


"""Преимущества"""


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ('icon', 'title', 'text')


# class FavoriteSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Favorite
#         fields = '__all__'
#
#     def create(self, validated_data):
#         post = validated_data.get('post')
#         favorite = Favorite.objects.get_or_create(post=post)[0]
#         favorite.favorites = True if favorite.favorites is False else False
#         favorite.save()
#         return favorite


"""Избранные"""
class FavProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'new_price', 'sale', 'favorites', 'new', 'hit', 'size')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation




"""товары этой коллекции"""


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('id', )


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance.product.all(), many=True).data
        return representation




"""Обратный звонок"""


class BackCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackCall
        fields = ('name', 'number', 'types')


"""Информация юзера"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'





