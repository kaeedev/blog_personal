from django.db import models
from django.utils.timezone import now
from django.utils.text import slugify
from thumbnails.fields import ImageField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField('Titulo', max_length=200)
    slug = models.SlugField('Slug', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    blog_image = ImageField('Portada del post',upload_to='post/images/', null=True, blank=True)
    content = RichTextField('Contenido')
    created_at = models.DateTimeField('Fecha de creación', default=now, editable=False)
    updated_at = models.DateTimeField('Fecha de actualización', auto_now=True)
    show_home = models.BooleanField('Mostrar en la home', default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # Genera el slug a partir del título
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

