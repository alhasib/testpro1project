# Generated by Django 3.1.4 on 2020-12-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpro1app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
