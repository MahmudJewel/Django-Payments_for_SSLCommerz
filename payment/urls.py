from django.urls import path, include
from django.views.generic import TemplateView
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('success',TemplateView.as_view(template_name='success.html'), name='success'),
    path('fail',TemplateView.as_view(template_name='fail.html'), name='fail'),
    path('cancel',TemplateView.as_view(template_name='cancel.html'), name='cancel'),
]

