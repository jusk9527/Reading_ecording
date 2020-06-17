from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView


from tailf.views import tailf

urlpatterns = [
    path('tailf', tailf, name='tailf-url'),

    path('login', LoginView.as_view(template_name='login.html'), name='login-url'),
    path('logout', LogoutView.as_view(template_name='login.html'), name='logout-url'),
]