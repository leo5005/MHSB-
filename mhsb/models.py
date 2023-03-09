from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    title = models.CharField('タイトル', max_length=200, blank=True)
    content = models.TextField('本文', blank=True)
    created = models.DateTimeField('作成日', default=timezone.now)
    picture = models.ImageField(upload_to = 'images', verbose_name='画像', blank=True)
    
    def __str__(self):
        return self.title