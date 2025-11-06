from django.contrib import admin
from .models import SiteSettings, PortfolioSection, Project


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """サイト設定の管理画面設定"""
    list_display = ['site_name', 'site_description']
    
    def has_add_permission(self, request):
        # 既にサイト設定が存在する場合は追加を許可しない
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # サイト設定の削除を禁止
        return False


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
