from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Nombre del template
    context_object_name = 'posts'  # Nombre con el que se accederán las publicaciones en la plantilla
    paginate_by = 3  # Número de publicaciones por página

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Nombre del template para los detalles
    context_object_name = 'post'  # Nombre con el que se accederá a la publicación en la plantilla

    def get_queryset(self):
        return super().get_queryset().filter(slug=self.kwargs['slug']) #Para que machee por slug y no id