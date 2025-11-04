from django.contrib import admin
from .models import PortfolioSection, Project


@admin.register(PortfolioSection)
class PortfolioSectionAdmin(admin.ModelAdmin):
    """ポートフォリオセクションの管理画面設定"""
    list_display = ['section_type', 'title', 'order', 'is_active']
    list_filter = ['section_type', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """実績プロジェクトの管理画面設定"""
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'description', 'technologies']
    ordering = ['order', '-created_at']
