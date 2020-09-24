from django.db import models
from django.utils import timezone
from django import forms


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,blank=True, null=True)
    post = models.CharField(verbose_name='投稿者', max_length=50, null=True)
    text = models.TextField(verbose_name='テキスト', max_length=200, null=True)
    created_date = models.DateTimeField(verbose_name='作成日',default=timezone.now, null=True)
    published_date = models.DateTimeField(verbose_name='投稿日',blank=True, null=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=100, null=True, blank=True, default='既読完了')
    image = models.ImageField(verbose_name='画像', upload_to='media/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments',blank=True, null=True)
    author = models.CharField(verbose_name='投稿者', max_length=50, null=True)
    text = models.TextField(verbose_name='テキスト', max_length=200, null=True )
    created_date = models.DateTimeField(verbose_name='作成日', default=timezone.now, null=True)
    approved_comment = models.NullBooleanField(default=False, null=True)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)






