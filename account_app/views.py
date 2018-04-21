from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        myform = UserCreationForm(request.POST)
        if myform.is_valid():
            user = myform.save()
            # log user in
            login( request, user)

            return redirect("article_app:list")
    else:
        myform = UserCreationForm()

    return render(request,'account/signup.html', { 'form': myform })

def login_view(request):
    if request.method == 'POST':
        myform = AuthenticationForm(data=request.POST)
        if myform.is_valid():
            # log in User
            user = myform.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("article_app:list")
    else:
        myform = AuthenticationForm()

    return render(request, 'account/login.html', { 'form': myform })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("article_app:list")
