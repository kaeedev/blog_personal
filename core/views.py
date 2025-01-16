from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from blog.models import Post
from .models import Contact
from django.views.generic.edit import FormView
from .forms import ContactForm, UserRegisterForm, LoginForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout



class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(show_home=True)
        return context



class ContactoForm(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        comentario = form.cleaned_data['comentario']
        message_content = f'{nombre} con email {email} ha escrito lo siguiente: {comentario}'

        Contact.objects.create(
        nombre=nombre,
        email=email,
        comentario=comentario
        )

        success = send_mail(
            'Formulario de contacto de mi Web',
            message_content,
            'lalbertohab@gmail.com',
            ['l.alberto3.albvisop@hotmail.com'],
            fail_silently=False
        )
        return super().form_valid(form)
    


class RegisterView(FormView):
    template_name = 'core/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('core:login')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']

        user = User.objects.create_user(username, email, password2)
        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.save()

        # Agrega un mensaje de éxito al contexto
        self.extra_context = {'success': 'Usuario creado correctamente'}
        return super().form_valid(form)

    def form_invalid(self, form):
        # Agrega el formulario y un mensaje de error al contexto
        self.extra_context = {'form': form, 'error': True}
        return super().form_invalid(form)

from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from .forms import LoginForm

class LoginView(FormView):
    template_name = 'core/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse('core:home'))
        else:
            return self.render_to_response(self.get_context_data(
                form=form,
                error=True,
                error_message='Usuario no válido'
            ))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(
            form=form,
            error=True
        ))

def logout_view(request):
    logout(request)
    return redirect(reverse('core:home'))
