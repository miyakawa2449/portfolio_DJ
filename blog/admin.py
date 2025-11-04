from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ブログ記事の管理画面設定"""
    list_display = ['title', 'author', 'is_published', 'published_at', 'created_at']
    list_filter = ['is_published', 'created_at', 'published_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
