# Generated by Django 4.0.4 on 2022-05-31 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_favorite_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
