from django.urls import path, include
from django.views.generic import TemplateView
from .views import home, ssl_status, ssl_complete, success, fail, cancel

urlpatterns = [
    path('', home, name='home'),
    # path('success',TemplateView.as_view(template_name='success.html'), name='success'),
    # path('fail',TemplateView.as_view(template_name='fail.html'), name='fail'),
    # path('cancel',TemplateView.as_view(template_name='cancel.html'), name='cancel'),

    path('success',success, name='success'),
    path('fail',fail, name='fail'),
    path('cancel',cancel, name='cancel'),
    path('status',ssl_status, name='status'),
    path('complete/<val_id>/<tran_id>/',ssl_complete, name='ssl_complete'),
]

