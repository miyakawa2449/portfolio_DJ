from .models import SiteSettings


def site_settings(request):
    """全テンプレートでサイト設定を使えるようにするコンテキストプロセッサ"""
    try:
        settings = SiteSettings.objects.first()
        if not settings:
            # サイト設定が存在しない場合はデフォルト値を使用
            settings = SiteSettings(
                site_name='Miyakawa Code',
                site_description='ウェブエンジニアのポートフォリオ & 技術ブログ'
            )
    except:
        # エラー時もデフォルト値を使用
        settings = SiteSettings(
            site_name='Miyakawa Code',
            site_description='ウェブエンジニアのポートフォリオ & 技術ブログ'
        )
    
    return {
        'site_settings': settings
    }