# Generated by Django 5.0.2 on 2024-03-01 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://icones.pro/wp-content/uploads/2021/04/icone-de-nourriture-grise-symbole-png.png', max_length=500),
        ),
    ]
