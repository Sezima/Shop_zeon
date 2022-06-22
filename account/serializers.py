from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import MyUser
from .utils import send_activation_code


class RegisterSerializer(serializers.ModelSerializer):
    """регистрация"""
    password = serializers.CharField(max_length=6, write_only=True)
    password_confirm = serializers.CharField(max_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'password_confirm')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Password not right')
        return validated_data

    def create(self, validated_data):
        """когда сохраняем обьект"""
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        send_activation_code(email=user.email,
                             activation_code=user.activation_code)
        return user

    def save(self, commit=True):
        user = MyUser.objects.create_user(**self.validated_data)
        send_activation_code(user.email, user.activation_code)
        return user


class LoginSerializer(serializers.Serializer):
    """логин"""
    email = serializers.EmailField()
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                message = 'Unable to login'
                raise serializers.ValidationError(message,
                                                  code='authorization')
        else:
            message = 'Must include "email" and "password".'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs
#     attrs == validate_data
