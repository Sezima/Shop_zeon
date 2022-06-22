import os
from django.core.exceptions import ValidationError


def validate_file(value):
    """валидация"""
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Файл с таким расширением не доступен.')
