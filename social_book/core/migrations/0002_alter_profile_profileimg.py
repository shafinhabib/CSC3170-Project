# Generated by Django 4.2.7 on 2023-11-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-profile-picture.webp', upload_to='profile_images'),
        ),
    ]