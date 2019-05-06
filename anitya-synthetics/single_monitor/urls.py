from django.urls import path

from . import views

app_name = 'single_monitor'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('ping/', views.PingView.as_view(), name='ping'),
    path('port/', views.PortView.as_view(), name='port'),
    path('url/', views.UrlView.as_view(), name='url'),
    path('dns/', views.DnsView.as_view(), name='dns'),
    path('domain/', views.DomainView.as_view(), name='domain'),
    path('cert/', views.CertView.as_view(), name='cert'),
]
