# Generated by Django 3.1.1 on 2020-10-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0013_auto_20200929_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='SorlPhoto/%Y', verbose_name='IMAGE'),
        ),
    ]
