"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings

from .views import (
    home ,
    about ,
    contact
    )
from blog_posts.views import post_create
from search.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abouts/', about , name='abouts'),
    path('contact/', contact , name='contact'),
    path('', home ,name='home'),
    path('search/', search , name='search'),
    path('post_new/' , post_create ,name='new_post'),
    path('' ,include('blog_posts.urls')),


]




if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
