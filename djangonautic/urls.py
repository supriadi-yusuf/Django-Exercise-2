"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from article_app import views as view_article

from django.contrib.staticfiles.urls import staticfiles_urlpatterns # add by spd for accessing static files
from django.conf.urls.static import static # add by spd for accessing media files
from django.conf import settings # add by spd for accessing media files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include('article_app.urls')),
    path('account/', include('account_app.urls')),
    path('', view_article.list_article, name = "home"),
]

urlpatterns += staticfiles_urlpatterns() # add by spd for accessing static files
urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # add by spd for accessing media files
