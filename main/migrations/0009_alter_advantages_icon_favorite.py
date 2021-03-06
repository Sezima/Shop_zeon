# Generated by Django 4.0.4 on 2022-05-31 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_product_price_alter_advantages_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantages',
            name='icon',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='main.product')),
            ],
        ),
    ]
