# Generated by Django 3.1.1 on 2020-10-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='petscategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petname', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='register',
            name='role',
            field=models.CharField(choices=[('Vetnarian', 'Vetnarian'), ('Pet Boarder', 'Pet Boarder'), ('Pet Groomer', 'Pet Groomer'), ('Dog Trainer', 'Dog Trainer'), ('Buyer/seller', 'Buyer/seller')], default='Vetnarian', max_length=67),
        ),
    ]
