# Generated by Django 5.1.2 on 2024-12-02 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0005_rename_initials_profile_avatar_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
