# Generated by Django 2.2.4 on 2019-09-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(default='media/img/destination_3.jpg', upload_to='img'),
        ),
    ]
