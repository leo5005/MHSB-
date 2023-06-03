from django.db import models
from django.conf import settings
from django.utils import timezone

class Post_1(models.Model):
    user = models.CharField(max_length=30, default='名無しのハンター')
    content = models.TextField('本文', null=False, max_length=1000)
    created = models.DateTimeField('作成日', default=timezone.now)
    picture = models.ImageField(upload_to = 'images', verbose_name='画像', blank=True)
    
    class Meta:
        pass
    
    def __str__(self):
        return self.user
    
class Comment_1(models.Model):
    user = models.CharField('名前', max_length=30, default='名無しのハンター')
    message = models.TextField('本文', null=False, max_length=1000)
    target = models.ForeignKey(Post_1, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    class Meta:
        ordering = ('-created_at',) 
    
    def __str__(self):
        return self.message[:20]    
    
    
    
class Post_2(models.Model):
    user = models.CharField(max_length=30, default='名無しのハンター')
    content = models.TextField('本文', null=False, max_length=1000)
    created = models.DateTimeField('作成日', default=timezone.now)
    picture = models.ImageField(upload_to = 'images', verbose_name='画像', blank=True)
    
    class Meta:
        pass
    
    def __str__(self):
        return self.user
    
class Comment_2(models.Model):
    user = models.CharField('名前', max_length=30, default='名無しのハンター')
    message = models.TextField('本文', null=False, max_length=1000)
    target = models.ForeignKey(Post_2, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    class Meta:
        ordering = ('-created_at',) 

    def __str__(self):
        return self.message[:20]    
    
class Post_3(models.Model):
    user = models.CharField(max_length=30, default='名無しのハンター')
    content = models.TextField('本文', null=False, max_length=1000)
    created = models.DateTimeField('作成日', default=timezone.now)
    picture = models.ImageField(upload_to = 'images', verbose_name='画像', blank=True)
    
    class Meta:
        pass
    
    def __str__(self):
        return self.user
    
class Comment_3(models.Model):
    user = models.CharField('名前', max_length=30, default='名無しのハンター')
    message = models.TextField('本文', null=False, max_length=1000)
    target = models.ForeignKey(Post_3, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    class Meta:
        ordering = ('-created_at',) 
    
    def __str__(self):
        return self.message[:20]    
    
class Post_4(models.Model):
    user = models.CharField(max_length=30, default='名無しのハンター')
    content = models.TextField('本文', null=False, max_length=1000)
    created = models.DateTimeField('作成日', default=timezone.now)
    picture = models.ImageField(upload_to = 'images', verbose_name='画像', blank=True)
    
    class Meta:
        pass
    
    def __str__(self):
        return self.user
    
class Comment_4(models.Model):
    user = models.CharField('名前', max_length=30, default='名無しのハンター')
    message = models.TextField('本文', null=False, max_length=1000)
    target = models.ForeignKey(Post_4, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    class Meta:
        ordering = ('-created_at',) 
    
    def __str__(self):
        return self.message[:20]    