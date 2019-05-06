from django.urls import path

from . import views

app_name = 'security_monitor'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('falsification/', views.IndexView.as_view(), name='falsification'),
    path('vulnerability', views.IndexView.as_view(), name='vulnerability'),
]
