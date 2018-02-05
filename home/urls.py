from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('keyboard/', views.keyboard, name='keyboard'),
    path('message', views.message ),
    path('webhook', views.webhook ),
]