# Generated by Django 4.0.4 on 2022-05-31 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_advantages_icon_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='favorite',
        ),
    ]
