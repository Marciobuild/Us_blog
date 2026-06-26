# urls.py
from django.urls import path
from . import views
from .views import CriarPost, AtualizarPost, DeletarPost

urlpatterns = [
    path("home/", views.home, name='home'),
    path("detalhes/<int:pk>/", views.PostDetalhes, name='PostDetalhes'),
    path("criar/", CriarPost.as_view(), name='CriarPost'),
    path('atualizar/<int:pk>/', AtualizarPost.as_view(), name='AtualizarPost'),
    path('deletar/<int:pk>/', DeletarPost.as_view(), name='DeletarPost'),
    path('portfolio/', views.portfolio, name='portfolio'),
]