# views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Category, Post, Tag

import logging

logger = logging.getLogger('django')


def _published_posts():
    return Post.objects.filter(foi_postado=True).select_related('categoria').prefetch_related('tags')


def home(request):
    posts = _published_posts()
    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('categoria', '').strip()
    tag_slug = request.GET.get('tag', '').strip()

    active_category = None
    active_tag = None

    if query:
        posts = posts.filter(
            Q(titulo__icontains=query) | Q(conteudo__icontains=query)
        )

    if category_slug:
        active_category = Category.objects.filter(slug=category_slug).first()
        if active_category:
            posts = posts.filter(categoria=active_category)

    if tag_slug:
        active_tag = Tag.objects.filter(slug=tag_slug).first()
        if active_tag:
            posts = posts.filter(tags=active_tag)

    context = {
        'posts': posts,
        'query': query,
        'active_category': active_category,
        'active_tag': active_tag,
    }
    return render(request, 'posts/home.html', context)


def PostDetalhes(request, pk):
    post = get_object_or_404(_published_posts(), pk=pk)
    return render(request, 'posts/PostDetalhes.html', {'post': post})


class CriarPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'conteudo', 'categoria', 'tags', 'foi_postado']
    template_name = 'posts/CriarPost.html'
    success_url = reverse_lazy('home')


class AtualizarPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'conteudo', 'categoria', 'tags', 'foi_postado']
    template_name = 'posts/CriarPost.html'
    success_url = reverse_lazy('home')


class DeletarPost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/Deletar.html'
    success_url = reverse_lazy('home')
