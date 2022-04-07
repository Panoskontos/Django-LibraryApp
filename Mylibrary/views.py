from django.shortcuts import redirect, render
from .forms import *
from .models import *
# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Mylibrary/home.html', {})


@login_required(login_url='login')
def AuthorRegister(request):
    form = AuthorRegistartionForm()
    if request.method == 'POST':
        form = AuthorRegistartionForm(request.POST)
        if form.is_valid():
            form.save()

        # get this new user
        username = form.cleaned_data.get('username')
        user = CustomUser.objects.get(username=username)
        # make him an author
        user.user_type = 'Author'
        user.save()

        # Create new author
        author = Author(user=user, name=username)
        author.save()
        return redirect('home')

    return render(request, 'Mylibrary/Register.html', {'form': form})


def PublisherRegister(request):
    form = PublisherForm()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()

        # get this new user
        username = form.cleaned_data.get('username')
        user = CustomUser.objects.get(username=username)
        # make him an author
        user.user_type = 'Publisher'
        user.save()

        # Create new author
        publisher = Publisher(user=user, name=username)
        publisher.save()
        return redirect('home')

    return render(request, 'Mylibrary/Register.html', {'form': form})


def Login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # grab username, password
            username = request.POST.get('username')
            password = request.POST.get('password')

            custom_user = CustomUser.objects.get(
                username=username, password=password)
            print(custom_user)
            if custom_user is None:
                return redirect('login')
            else:
                # authenticate user
                print(custom_user.user_type)
                auth.login(request, custom_user)
                return redirect('home')
    return render(request, 'Mylibrary/Register.html', {'form': form})
