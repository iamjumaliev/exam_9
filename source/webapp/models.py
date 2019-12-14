from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    picture = models.ImageField(null=False, blank=False, upload_to='pics', verbose_name='Фотография')
    label = models.CharField(max_length=2000, null=False, blank=False, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    author = models.ForeignKey(User,related_name='photo_author',on_delete=models.PROTECT,
                                    verbose_name='Автор',null=False,blank=False)

class Comment(models.Model):
    text = models.CharField(max_length=2000, null=False, blank=False, verbose_name='Текст')
    picture = models.ForeignKey('webapp.Photo',null=False, blank=False, verbose_name='Фотография',
                                related_name = 'comment_picture',on_delete=models.PROTECT)
    author = models.ForeignKey(User,related_name='comment_author',on_delete=models.PROTECT,
                                    verbose_name='Автор',null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
# Create your models here.
