# Generated by Django 2.2.3 on 2019-08-05 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190805_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='画像'),
        ),
    ]
