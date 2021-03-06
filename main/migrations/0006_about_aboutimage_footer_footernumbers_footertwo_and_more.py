# Generated by Django 4.0.4 on 2022-05-30 06:31

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import fontawesome_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_helpimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='abouts')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.about')),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', fontawesome_5.fields.IconField(blank=True, max_length=60, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('number', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='FooterNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.footer')),
            ],
        ),
        migrations.CreateModel(
            name='FooterTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
                ('mail', models.URLField(blank=True)),
                ('insta', models.URLField(blank=True)),
                ('telegram', models.URLField(blank=True)),
                ('whatsapp', models.CharField(blank=True, max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('vendorcode', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('old_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='????????????')),
                ('description', models.TextField(blank=True, verbose_name='????????????????')),
                ('material', models.CharField(max_length=200)),
                ('structure', models.CharField(max_length=200)),
                ('new', models.BooleanField(default=False)),
                ('hit', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.product')),
            ],
        ),
        migrations.DeleteModel(
            name='HelpImage',
        ),
        migrations.AddField(
            model_name='help',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='advantages',
            name='icon',
            field=fontawesome_5.fields.IconField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='collection_image'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=220, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='main',
            name='link',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='collections',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.collection'),
        ),
    ]
