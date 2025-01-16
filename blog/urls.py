from django.urls import path
from .views import PostDetailView, PostListView
app_name='blog'

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),  # Lista de publicaciones
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),  # Detalle de publicación
]