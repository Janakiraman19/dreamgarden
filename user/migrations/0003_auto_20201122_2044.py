# Generated by Django 3.1.1 on 2020-11-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201122_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogs_advert',
            name='customer',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
