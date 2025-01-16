from django.contrib import admin

# Register your models here.

from blog.models import Post
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django import forms

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'blog_image', 'content', 'show_home']
        widgets = {
            'content': CKEditorWidget(),
        }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display= ['title', 'author', 'slug', 'content', 'created_at', 'updated_at', 'show_home']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            # Restringe el campo 'author' al usuario registrado
            if not request.user.is_superuser:
                kwargs["queryset"] = User.objects.filter(pk=request.user.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):
        # En caso de creación, asigna automáticamente el usuario como autor
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Superusuarios ven todo; usuarios normales solo ven sus posts
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author=request.user)
    
    def has_change_permission(self, request, obj=None):
        # Permite editar solo si el usuario es el autor o superusuario
        if request.user.is_superuser:
            return True
        if obj is not None and obj.author == request.user:
            return True
        return False
    