from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('what-is/', views.what_is, name='what_is'),
    path('contact/', views.contact, name='contact'),
    path('law-enforcement/', views.law_enforcement, name='law_enforcement'),
    path('enforcer/', views.enforcer, name='enforcer'),
    path('hotline/', views.hotline, name='hotline'),
    path('message/', views.message, name='message'), 
]