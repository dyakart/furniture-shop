# Generated by Django 4.2.11 on 2024-10-16 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзину', 'verbose_name_plural': 'Корзины'},
        ),
    ]
