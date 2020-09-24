# Generated by Django 2.2.3 on 2019-08-05 01:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=50, null=True, verbose_name='投稿者')),
                ('text', models.TextField(max_length=200, null=True, verbose_name='テキスト')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('good', models.IntegerField(blank=True, default=0, null=True)),
                ('read', models.IntegerField(blank=True, default=0, null=True)),
                ('readtext', models.CharField(blank=True, default='既読完了', max_length=100, null=True)),
                ('images', models.ImageField(upload_to='', verbose_name='画像')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, null=True, verbose_name='投稿者')),
                ('text', models.TextField(max_length=200, null=True, verbose_name='テキスト')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('approved_comment', models.BooleanField(default=False, null=True)),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
        ),
    ]