from django.urls import path
from .views import HomeView, ContactoForm, RegisterView, LoginView, logout_view

app_name='core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactoForm.as_view(), name='contact' ),
    path('register/', RegisterView.as_view(), name='register' ),
    path('login/', LoginView.as_view(), name='login' ),
    path('logout/', logout_view, name= 'logout')
]