# Generated by Django 5.1.2 on 2024-10-28 15:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.CharField(default=2, max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='users',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
