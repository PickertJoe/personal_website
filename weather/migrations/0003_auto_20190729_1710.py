# Generated by Django 2.2.3 on 2019-07-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_city_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
