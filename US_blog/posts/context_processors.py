from django.db.models import Count, Q

from .models import Category, Post, Tag


def sidebar_context(request):
    published = Post.objects.filter(foi_postado=True)
    return {
        'sidebar_recent_posts': published[:5],
        'sidebar_categories': Category.objects.annotate(
            post_count=Count('posts', filter=Q(posts__foi_postado=True))
        ).filter(post_count__gt=0),
        'sidebar_tags': Tag.objects.annotate(
            post_count=Count('posts', filter=Q(posts__foi_postado=True))
        ).filter(post_count__gt=0)[:12],
    }
