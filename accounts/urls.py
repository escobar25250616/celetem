from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('merci/', views.merci_view, name='merci'),
]
