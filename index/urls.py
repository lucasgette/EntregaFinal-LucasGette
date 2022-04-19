
from django.urls import path
from .views import home
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about')
]
