"""loveshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
]

if settings.APP_ENV == 'docker':
    urlpatterns = urlpatterns \
                  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
                  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
