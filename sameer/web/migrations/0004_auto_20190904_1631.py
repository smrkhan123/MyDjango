# Generated by Django 2.2.4 on 2019-09-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190904_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(default='images/contact.jpg', upload_to='pics'),
        ),
    ]
