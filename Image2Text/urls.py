"""
URL configuration for Image2Text project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# image2text/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Image2Text.img2txtapp.views import extract_text

urlpatterns = [
    path('', extract_text, name='extract_text'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
