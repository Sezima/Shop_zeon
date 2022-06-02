from rest_framework import serializers

from .models import *


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = ('title', 'text')


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('image', 'title', 'text')


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('question', 'answer')


class HelpImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpImage
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title',  'text')


class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = '__all__'


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


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ('logo', 'text', 'number')


class FooterTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterTwo
        fields = ('number', 'telegram', 'instagram', 'email', 'whatsapp')


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'




    def create(self, validated_data):
        post = validated_data.get('post')
        favorite = Favorite.objects.get_or_create(post=post)[0]
        favorite.favorite = validated_data['favorite']
        favorite.save()
        return favorite
















