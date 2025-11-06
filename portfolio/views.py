from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
    PortfolioSection, Project, HeroSection, AboutSection, 
    Feature, Skill, Achievement, CTASection, ContactSection
)


class PortfolioView(TemplateView):
    """ポートフォリオトップページビュー"""
    template_name = 'portfolio/index_figma.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 新しいモデル構造からデータを取得
        try:
            context['hero_section'] = HeroSection.objects.first()
        except HeroSection.DoesNotExist:
            context['hero_section'] = None
            
        try:
            context['about_section'] = AboutSection.objects.first()
        except AboutSection.DoesNotExist:
            context['about_section'] = None
            
        context['features'] = Feature.objects.filter(is_active=True).order_by('order')
        context['skills'] = Skill.objects.filter(is_active=True).order_by('order')
        context['achievements'] = Achievement.objects.filter(is_active=True).order_by('order')
        context['projects'] = Project.objects.filter(is_active=True).order_by('order')
        
        try:
            context['cta_section'] = CTASection.objects.first()
        except CTASection.DoesNotExist:
            context['cta_section'] = None
            
        try:
            context['contact_section'] = ContactSection.objects.first()
        except ContactSection.DoesNotExist:
            context['contact_section'] = None
        
        # 旧モデル（互換性のため）
        sections = PortfolioSection.objects.filter(is_active=True).order_by('order')
        context['sections'] = sections
        
        return context
