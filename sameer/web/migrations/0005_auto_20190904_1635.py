# Generated by Django 2.2.4 on 2019-09-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20190904_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(default='', upload_to='pics'),
        ),
    ]
