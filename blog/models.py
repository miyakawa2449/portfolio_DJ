from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """ブログ記事モデル（基本機能のみ）"""
    title = models.CharField(max_length=200, verbose_name='タイトル')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='スラッグ')
    content = models.TextField(verbose_name='本文')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='著者')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    published_at = models.DateTimeField(blank=True, null=True, verbose_name='公開日時')
    is_published = models.BooleanField(default=False, verbose_name='公開状態')
    
    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'
        ordering = ['-published_at', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """公開時に公開日時を自動設定"""
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
