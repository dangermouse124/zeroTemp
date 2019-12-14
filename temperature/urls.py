from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('ajaxTemp', views.ajaxTemp, name='ajaxTemp'),
    path('gauge/', views.gauge, name='gauge'),
    path('gaugeTest/', views.gaugeTest, name='gaugeTest'),
]