# Generated by Django 4.0.6 on 2022-07-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_user_productsmodel_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodel',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
