# Generated by Django 3.1.1 on 2020-11-23 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20201122_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='birds_advert',
            name='user_id',
        ),
        migrations.AddField(
            model_name='birds_advert',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='birds_advert',
            name='location',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
