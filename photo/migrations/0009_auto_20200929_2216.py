# Generated by Django 3.1.1 on 2020-09-29 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0008_auto_20200929_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='upload_dt',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 29, 13, 16, 10, 976974, tzinfo=utc), null=True, verbose_name='UPLOAD DATE'),
        ),
    ]
