from django.db import models


class SiteSettings(models.Model):
    """サイト全体の設定を管理するモデル"""
    site_name = models.CharField(max_length=200, default='Miyakawa Code', verbose_name='サイト名')
    site_description = models.CharField(max_length=500, blank=True, verbose_name='サイト説明')
    site_keywords = models.CharField(max_length=500, blank=True, verbose_name='SEOキーワード', help_text='カンマ区切りで入力')
    footer_text = models.CharField(max_length=200, blank=True, verbose_name='フッターテキスト')
    
    class Meta:
        verbose_name = 'サイト設定'
        verbose_name_plural = 'サイト設定'
    
    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        # サイト設定は1つのみ存在するように制御
        if not self.pk and SiteSettings.objects.exists():
            # 既存のオブジェクトがある場合は、それを更新
            self.pk = SiteSettings.objects.first().pk
        super().save(*args, **kwargs)


class PortfolioSection(models.Model):
    """ポートフォリオのセクション管理モデル"""
    SECTION_TYPES = [
        ('about', 'About'),
        ('service', 'Service'),
        ('skill', 'Skill'),
        ('project', '実績'),
        ('contact', 'Contact'),
    ]
    
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, unique=True, verbose_name='セクションタイプ')
    title = models.CharField(max_length=100, verbose_name='タイトル')
    subtitle = models.CharField(max_length=200, blank=True, verbose_name='サブタイトル')
    content = models.TextField(verbose_name='内容')
    order = models.IntegerField(default=0, verbose_name='表示順')
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    
    class Meta:
        verbose_name = 'ポートフォリオセクション'
        verbose_name_plural = 'ポートフォリオセクション'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"


class Project(models.Model):
    """実績プロジェクトモデル"""
    title = models.CharField(max_length=200, verbose_name='プロジェクト名')
    description = models.TextField(verbose_name='説明')
    technologies = models.CharField(max_length=500, verbose_name='使用技術', help_text='カンマ区切りで入力')
    project_url = models.URLField(blank=True, verbose_name='プロジェクトURL')
    github_url = models.URLField(blank=True, verbose_name='GitHub URL')
    order = models.IntegerField(default=0, verbose_name='表示順')
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    
    class Meta:
        verbose_name = '実績プロジェクト'
        verbose_name_plural = '実績プロジェクト'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        """使用技術をリストで返す"""
        return [tech.strip() for tech in self.technologies.split(',')]
