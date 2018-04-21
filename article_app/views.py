from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.
def list_article(request):
    articles = Article.objects.all().order_by('date')
    class Tambah:
        i=0

        def get(self):
            self.i += 1
            return self.i

    tambah = Tambah()
    return render(request,'article/article_list.html', { 'article_list': articles,
    'tambah': tambah})

def details(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'article/article_detail.html', { 'article': article })

# @login_required(login_url="/account/login/")
@login_required(login_url="account_app:login")
def create_article(request):
    if request.method == "POST":
        myform = forms.CreateArticle( request.POST, request.FILES)
        if myform.is_valid():
            # save form
            my_instance = myform.save(commit=False)
            my_instance.author = request.user
            my_instance.save()
            return redirect("article_app:list")
    else:
        myform = forms.CreateArticle()

    return render( request, 'article/article_create.html', { 'form': myform })
