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
        fields = ('question', 'answer', 'image')


# class HelpImageSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = HelpImage
    #     fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('title',  'text')


class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImage
        fields = '__all__'


