# Generated by Django 3.1.1 on 2020-09-29 13:18

from django.db import migrations
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_auto_20200929_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photo.fields.ThumbnailImageField(null=True, upload_to='photo/%Y/%m'),
        ),
    ]
