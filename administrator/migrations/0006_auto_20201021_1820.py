# Generated by Django 3.1.1 on 2020-10-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_remove_register_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='pets_sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petname', models.CharField(max_length=100)),
                ('breedname', models.CharField(max_length=100)),
                ('image', models.ImageField(max_length=80, upload_to='')),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='breeds',
            name='petsname',
            field=models.CharField(max_length=100),
        ),
    ]
