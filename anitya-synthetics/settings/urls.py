from django.urls import path

from . import views

app_name = 'settings'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('hoge/', views.IndexView.as_view(), name='index'),
    path('fuga/', views.IndexView.as_view(), name='index'),
    path('moga/', views.IndexView.as_view(), name='index'),
]
