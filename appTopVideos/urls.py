from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('videos', views.index_videos, name='videos'),
    path('plataformas', views.index_plataformas, name='plataformas'),
    path('categorias', views.index_categorias, name='categorias'),
    path('videos/<int:video_id>/', views.show_video, name='video'),
    path('categorias/<int:categoria_id>', views.show_categoria, name='categoria'),
    path('plataformas/<int:plataforma_id>', views.show_plataforma, name='plataforma'),
]