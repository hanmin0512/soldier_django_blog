# Generated by Django 3.1.1 on 2020-09-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20200927_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='upload_dt',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='UPLOAD DATE'),
        ),
    ]