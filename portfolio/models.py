from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


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


class HeroSection(models.Model):
    """ヒーローセクション管理モデル"""
    main_title = models.TextField(default='ビジネス課題から実\n装まで\n一人で解決する\nエンジニア', verbose_name='メインタイトル', help_text='改行位置で分割されます')
    
    subtitle_tech = models.CharField(max_length=100, default='Python 3.13 • Flask 3.1.2', verbose_name='技術情報')
    
    author_name = models.CharField(max_length=50, default='宮川 剛', verbose_name='氏名')
    author_description = models.CharField(max_length=200, default='14年の経験。プログラミング歴から起業ビジネスまで幅広い解決力', verbose_name='自己紹介')
    
    # 画像関連フィールド
    hero_image = ProcessedImageField(
        upload_to='hero/', 
        processors=[ResizeToFill(600, 384)],  # 600x384pxに自動リサイズ・クロップ
        format='JPEG',
        options={'quality': 90},
        blank=True, 
        null=True, 
        verbose_name='ヒーロー画像',
        help_text='アップロード時に自動的に600px × 384px（アスペクト比 25:16）にリサイズされます'
    )
    hero_image_alt = models.CharField(
        max_length=200, 
        blank=True, 
        verbose_name='画像のalt属性',
        help_text='アクセシビリティのため、画像の説明を入力してください'
    )
    
    cta_primary_text = models.CharField(max_length=50, default='サービス詳細', verbose_name='プライマリボタンテキスト')
    cta_primary_link = models.CharField(max_length=100, default='#services', verbose_name='プライマリボタンリンク')
    cta_secondary_text = models.CharField(max_length=50, default='お問い合わせ', verbose_name='セカンダリボタンテキスト')
    cta_secondary_link = models.CharField(max_length=100, default='#contact', verbose_name='セカンダリボタンリンク')
    
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    
    class Meta:
        verbose_name = 'ヒーローセクション'
        verbose_name_plural = 'ヒーローセクション'
    
    def __str__(self):
        return f"ヒーローセクション - {self.author_name}"
    
    def save(self, *args, **kwargs):
        # ヒーローセクションは1つのみ存在するように制御
        if not self.pk and HeroSection.objects.exists():
            self.pk = HeroSection.objects.first().pk
        super().save(*args, **kwargs)
    
    def get_title_lines(self):
        """メインタイトルを行ごとのリストで返す"""
        return self.main_title.split('\n')


class AboutSection(models.Model):
    """Aboutセクション管理モデル"""
    title = models.CharField(max_length=100, default='About', verbose_name='セクションタイトル')
    subtitle = models.CharField(max_length=200, blank=True, verbose_name='サブタイトル')
    
    profile_image = models.ImageField(upload_to='about/', blank=True, verbose_name='プロフィール画像')
    
    introduction = models.TextField(verbose_name='自己紹介文')
    career_summary = models.TextField(verbose_name='経歴要約')
    philosophy = models.TextField(blank=True, verbose_name='仕事への想い・哲学')
    
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    
    class Meta:
        verbose_name = 'Aboutセクション'
        verbose_name_plural = 'Aboutセクション'
    
    def __str__(self):
        return f"About - {self.title}"
    
    def save(self, *args, **kwargs):
        # Aboutセクションは1つのみ存在するように制御
        if not self.pk and AboutSection.objects.exists():
            self.pk = AboutSection.objects.first().pk
        super().save(*args, **kwargs)


class Feature(models.Model):
    """他のエンジニアとの違い（3つの特徴）モデル"""
    title = models.CharField(max_length=100, verbose_name='特徴タイトル')
    description = models.TextField(verbose_name='説明')
    icon_class = models.CharField(max_length=100, blank=True, verbose_name='アイコンクラス', 
                                help_text='SVGアイコンのクラス名（任意）')
    order = models.IntegerField(default=0, verbose_name='表示順')
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    
    class Meta:
        verbose_name = '特徴'
        verbose_name_plural = '特徴（他のエンジニアとの違い）'
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    """スキルモデル"""
    name = models.CharField(max_length=100, verbose_name='スキル名')
    experience_years = models.IntegerField(verbose_name='経験年数')
    proficiency_percentage = models.IntegerField(verbose_name='習熟度（%）', 
                                               help_text='0-100の数値で入力')
    description = models.TextField(blank=True, verbose_name='詳細説明')
    order = models.IntegerField(default=0, verbose_name='表示順')
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    
    class Meta:
        verbose_name = 'スキル'
        verbose_name_plural = 'スキル'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.name} - {self.proficiency_percentage}%"


class Achievement(models.Model):
    """実績数値モデル"""
    title = models.CharField(max_length=100, verbose_name='指標名')
    value = models.CharField(max_length=20, verbose_name='数値', 
                           help_text='例: 100%, 50+, 100日, 14年')
    description = models.CharField(max_length=100, verbose_name='説明')
    icon_class = models.CharField(max_length=100, blank=True, verbose_name='アイコンクラス')
    order = models.IntegerField(default=0, verbose_name='表示順')
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    
    class Meta:
        verbose_name = '実績指標'
        verbose_name_plural = '実績指標'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title}: {self.value}"


class Project(models.Model):
    """提供サービス・プロジェクトモデル（改良版）"""
    title = models.CharField(max_length=200, verbose_name='サービス・プロジェクト名')
    description = models.TextField(verbose_name='説明')
    technologies = models.CharField(max_length=500, verbose_name='使用技術・特徴', 
                                  help_text='カンマ区切りで入力')
    
    # 画像
    thumbnail_image = ProcessedImageField(
        upload_to='projects/', 
        processors=[ResizeToFill(400, 240)],  # 400x240pxに自動リサイズ・クロップ
        format='JPEG',
        options={'quality': 85},
        blank=True, 
        null=True, 
        verbose_name='サムネイル画像',
        help_text='アップロード時に自動的に400px × 240px（アスペクト比 5:3）にリサイズされます'
    )
    
    # リンク
    project_url = models.URLField(blank=True, verbose_name='プロジェクトURL')
    github_url = models.URLField(blank=True, verbose_name='GitHub URL')
    demo_url = models.URLField(blank=True, verbose_name='デモURL')
    
    # 管理用
    order = models.IntegerField(default=0, verbose_name='表示順')
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    is_featured = models.BooleanField(default=False, verbose_name='注目プロジェクト')
    
    # 時系列
    project_date = models.DateField(blank=True, null=True, verbose_name='プロジェクト実施日')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    
    class Meta:
        verbose_name = '提供サービス・プロジェクト'
        verbose_name_plural = '提供サービス・プロジェクト'
        ordering = ['order', '-project_date', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        """使用技術をリストで返す"""
        return [tech.strip() for tech in self.technologies.split(',')]


class CTASection(models.Model):
    """CTAセクション（Python チャレンジ等）管理モデル"""
    badge_text = models.CharField(max_length=100, default='🐍 Python 100日チャレンジ運行中！', 
                                verbose_name='バッジテキスト')
    main_title = models.CharField(max_length=100, default='毎日の学習で技術力を向上', 
                                verbose_name='メインタイトル')
    description = models.TextField(default='継続的な学習を通じて、最新のPython技術やAI/機械学習分野のスキルを日々更新しています。', 
                                 verbose_name='説明文')
    
    button_text = models.CharField(max_length=50, default='進捗を確認する', verbose_name='ボタンテキスト')
    button_link = models.CharField(max_length=100, default='/blog/', verbose_name='ボタンリンク')
    
    background_color = models.CharField(max_length=50, default='bg-gray-900', verbose_name='背景色（Tailwind）')
    text_color = models.CharField(max_length=50, default='text-white', verbose_name='文字色（Tailwind）')
    
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    
    class Meta:
        verbose_name = 'CTAセクション'
        verbose_name_plural = 'CTAセクション'
    
    def __str__(self):
        return f"CTA - {self.main_title}"
    
    def save(self, *args, **kwargs):
        # CTAセクションは1つのみ存在するように制御
        if not self.pk and CTASection.objects.exists():
            self.pk = CTASection.objects.first().pk
        super().save(*args, **kwargs)


class ContactSection(models.Model):
    """お問い合わせセクション管理モデル"""
    title = models.CharField(max_length=100, default='まずはお気軽にご相談ください', 
                           verbose_name='セクションタイトル')
    description = models.TextField(default='ビジネス課題の解決から技術的な実装まで、どんなご相談でもお気軽にお声がけください。', 
                                 verbose_name='説明文')
    
    # 連絡手段
    email_address = models.EmailField(default='contact@miyakawa.code', verbose_name='メールアドレス')
    email_button_text = models.CharField(max_length=50, default='メールでお問い合わせ', 
                                       verbose_name='メールボタンテキスト')
    
    slack_url = models.URLField(default='https://slack.com/intl/ja-jp/', verbose_name='Slack URL')
    slack_button_text = models.CharField(max_length=50, default='Slackでご相談', 
                                       verbose_name='Slackボタンテキスト')
    
    # その他の連絡手段（将来拡張用）
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='電話番号')
    linkedin_url = models.URLField(blank=True, verbose_name='LinkedIn URL')
    twitter_url = models.URLField(blank=True, verbose_name='Twitter URL')
    
    is_active = models.BooleanField(default=True, verbose_name='表示する')
    
    class Meta:
        verbose_name = 'お問い合わせセクション'
        verbose_name_plural = 'お問い合わせセクション'
    
    def __str__(self):
        return f"Contact - {self.title}"
    
    def save(self, *args, **kwargs):
        # お問い合わせセクションは1つのみ存在するように制御
        if not self.pk and ContactSection.objects.exists():
            self.pk = ContactSection.objects.first().pk
        super().save(*args, **kwargs)


# 旧モデル（互換性のため残す）
class PortfolioSection(models.Model):
    """旧ポートフォリオセクションモデル（非推奨）"""
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
        verbose_name = 'ポートフォリオセクション（旧）'
        verbose_name_plural = 'ポートフォリオセクション（旧）'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.get_section_type_display()} - {self.title}"