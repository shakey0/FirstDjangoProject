# Generated by Django 5.0.2 on 2024-03-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://via.placeholder.com/150', max_length=500),
        ),
    ]
