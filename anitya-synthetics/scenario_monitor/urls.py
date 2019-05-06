from django.urls import path

from . import views

app_name = 'scenario_monitor'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('step/', views.StepView.as_view(), name='step'),
    path('api/', views.ApiView.as_view(), name='api'),
]
