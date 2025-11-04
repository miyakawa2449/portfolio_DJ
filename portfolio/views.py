from django.shortcuts import render
from django.views.generic import TemplateView
from .models import PortfolioSection, Project


class PortfolioView(TemplateView):
    """ポートフォリオトップページビュー"""
    template_name = 'portfolio/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # アクティブなセクションを取得
        sections = PortfolioSection.objects.filter(is_active=True).order_by('order')
        context['sections'] = sections
        
        # セクションごとのデータを個別に取得
        for section in sections:
            context[f'{section.section_type}_section'] = section
        
        # 実績プロジェクトを取得
        context['projects'] = Project.objects.filter(is_active=True).order_by('order')
        
        return context
