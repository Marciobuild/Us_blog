from django.contrib import admin

from .models import Category, Post, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'foi_postado', 'data_de_criacao')
    list_filter = ('foi_postado', 'categoria', 'tags')
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}


admin.site.register(Category)
admin.site.register(Tag)
