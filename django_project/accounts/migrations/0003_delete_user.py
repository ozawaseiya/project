# Generated by Django 2.2.3 on 2019-08-04 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190804_1327'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
