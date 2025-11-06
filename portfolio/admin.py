from django.contrib import admin
from .models import (
    SiteSettings, HeroSection, AboutSection, Feature, Skill, 
    Achievement, Project, CTASection, ContactSection, PortfolioSection
)


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


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    """ヒーローセクションの管理画面設定"""
    list_display = ['author_name', 'is_active']
    fieldsets = (
        ('メインタイトル', {
            'fields': ('main_title',),
            'description': '改行を入れると、その位置で行が分かれて表示されます'
        }),
        ('技術情報', {
            'fields': ('subtitle_tech',)
        }),
        ('プロフィール', {
            'fields': ('author_name', 'author_description')
        }),
        ('ヒーロー画像', {
            'fields': ('hero_image', 'hero_image_alt'),
            'description': '推奨サイズ: 600px × 384px。alt属性は画像の説明として必須です。'
        }),
        ('CTAボタン', {
            'fields': (
                ('cta_primary_text', 'cta_primary_link'),
                ('cta_secondary_text', 'cta_secondary_link')
            )
        }),
        ('表示設定', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        # 既にヒーローセクションが存在する場合は追加を許可しない
        return not HeroSection.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # ヒーローセクションの削除を禁止
        return False


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    """Aboutセクションの管理画面設定"""
    list_display = ['title', 'is_active']
    fieldsets = (
        ('基本情報', {
            'fields': ('title', 'subtitle')
        }),
        ('プロフィール画像', {
            'fields': ('profile_image',)
        }),
        ('コンテンツ', {
            'fields': ('introduction', 'career_summary', 'philosophy')
        }),
        ('表示設定', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        # 既にAboutセクションが存在する場合は追加を許可しない
        return not AboutSection.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Aboutセクションの削除を禁止
        return False


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    """特徴の管理画面設定"""
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    ordering = ['order']
    search_fields = ['title', 'description']
    
    fieldsets = (
        ('基本情報', {
            'fields': ('title', 'description')
        }),
        ('デザイン', {
            'fields': ('icon_class',)
        }),
        ('表示設定', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """スキルの管理画面設定"""
    list_display = ['name', 'experience_years', 'proficiency_percentage', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    ordering = ['order']
    search_fields = ['name', 'description']
    
    fieldsets = (
        ('基本情報', {
            'fields': ('name', 'description')
        }),
        ('スキルレベル', {
            'fields': ('experience_years', 'proficiency_percentage')
        }),
        ('表示設定', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """実績指標の管理画面設定"""
    list_display = ['title', 'value', 'description', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']
    ordering = ['order']
    search_fields = ['title', 'description']
    
    fieldsets = (
        ('基本情報', {
            'fields': ('title', 'value', 'description')
        }),
        ('デザイン', {
            'fields': ('icon_class',)
        }),
        ('表示設定', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """提供サービス・プロジェクトの管理画面設定"""
    list_display = ['title', 'is_featured', 'order', 'is_active', 'project_date', 'created_at']
    list_editable = ['order', 'is_active', 'is_featured']
    list_filter = ['is_active', 'is_featured', 'created_at', 'project_date']
    search_fields = ['title', 'description', 'technologies']
    ordering = ['order', '-project_date', '-created_at']
    date_hierarchy = 'project_date'
    
    fieldsets = (
        ('基本情報', {
            'fields': ('title', 'description', 'technologies')
        }),
        ('画像', {
            'fields': ('thumbnail_image',)
        }),
        ('リンク', {
            'fields': ('project_url', 'github_url', 'demo_url')
        }),
        ('プロジェクト情報', {
            'fields': ('project_date',)
        }),
        ('表示設定', {
            'fields': ('order', 'is_active', 'is_featured')
        }),
    )


@admin.register(CTASection)
class CTASectionAdmin(admin.ModelAdmin):
    """CTAセクションの管理画面設定"""
    list_display = ['main_title', 'is_active']
    fieldsets = (
        ('バッジ', {
            'fields': ('badge_text',)
        }),
        ('メインコンテンツ', {
            'fields': ('main_title', 'description')
        }),
        ('ボタン', {
            'fields': ('button_text', 'button_link')
        }),
        ('デザイン', {
            'fields': ('background_color', 'text_color')
        }),
        ('表示設定', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        # 既にCTAセクションが存在する場合は追加を許可しない
        return not CTASection.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # CTAセクションの削除を禁止
        return False


@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    """お問い合わせセクションの管理画面設定"""
    list_display = ['title', 'email_address', 'is_active']
    fieldsets = (
        ('基本情報', {
            'fields': ('title', 'description')
        }),
        ('主要な連絡手段', {
            'fields': (
                ('email_address', 'email_button_text'),
                ('slack_url', 'slack_button_text')
            )
        }),
        ('その他の連絡手段', {
            'fields': ('phone_number', 'linkedin_url', 'twitter_url'),
            'classes': ('collapse',)
        }),
        ('表示設定', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        # 既にお問い合わせセクションが存在する場合は追加を許可しない
        return not ContactSection.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # お問い合わせセクションの削除を禁止
        return False


# 旧モデル（互換性のため残す）
@admin.register(PortfolioSection)
class PortfolioSectionAdmin(admin.ModelAdmin):
    """旧ポートフォリオセクションの管理画面設定（非推奨）"""
    list_display = ['section_type', 'title', 'order', 'is_active']
    list_filter = ['section_type', 'is_active']
    list_editable = ['order', 'is_active']
    ordering = ['order']
    
    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # 管理画面に警告を表示するためのカスタマイズも可能
        return qs