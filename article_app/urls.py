from django.urls import path, re_path
from . import views as view_article

app_name = 'article_app' # namespace for url's name

urlpatterns = [
    path('', view_article.list_article, name = 'list'),
    path('create/', view_article.create_article, name = 'create'),
    re_path(r'^(?P<slug>[\w-]+)/$', view_article.details, name = 'details'),
]
