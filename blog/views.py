from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    """ブログ記事一覧ビュー"""
    model = Post
    template_name = 'blog/post_list_figma.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        """公開済みの記事のみ表示"""
        return Post.objects.filter(is_published=True).order_by('-published_at')


class PostDetailView(DetailView):
    """ブログ記事詳細ビュー"""
    model = Post
    template_name = 'blog/post_detail_figma.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        """公開済みの記事のみ表示"""
        return Post.objects.filter(is_published=True)
