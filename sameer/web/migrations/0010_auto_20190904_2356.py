# Generated by Django 2.2.4 on 2019-09-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20190904_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(blank=True, default='', null=True, upload_to='pics'),
        ),
    ]
