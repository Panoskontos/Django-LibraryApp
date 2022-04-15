from distutils.util import change_root
from django.shortcuts import redirect, render
from .forms import *
from .models import *
# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .filters import *
import requests

# I edited this


@login_required(login_url='login')
def home(request):
    books = Book.objects.all()

    wishlist = Wishlist.objects.all()
    mydict = {}
    # O(n)
    for i in wishlist:
        mydict[i.user.username] = set()
    for i in wishlist:
        mydict[i.user.username].add(i.book.title)
    print(mydict)
    # wishlist = Wishlist.objects.all()
    # mydict = dict()
    # # O(n)
    # # create empty sets
    # for i in wishlist:
    #     mydict[i.user.username] = set()
    # # add to arrays
    # for i in wishlist:
    #     mydict[i.user.username].add(i.book.title)


# API
    url = "http://universities.hipolabs.com/search?country=United+Kingdom"
    r = requests.get(url)
    object = r.json()
    print(object)

    # print(mydict)
    context = {
        'wishlist': wishlist,
        'books': books,
        'mydict': mydict,


        # API data
        'object': object,
    }
    return render(request, 'Mylibrary/home.html', context)


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

        # Create new author
        author = Author(user=user, name=username)
        author.save()
        return redirect('home')

    return render(request, 'Mylibrary/Register.html', {'form': form})


def PublisherRegister(request):
    form = PublisherForm()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        # get password

        # MyCryptographicAlgorithm

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
        # MyCryptographicAlgorithm
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


@login_required(login_url='login')
def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'Mylibrary/add_book.html', {'form': form})


@login_required(login_url='login')
def delete_book(request, pk):
    object = Book.objects.get(id=pk)
    if request.method == 'POST':
        object.delete()
        return redirect('home')
    return render(request, 'Mylibrary/delete_book.html', {'object': object})


@login_required(login_url='login')
def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'Mylibrary/add_book.html', {'form': form})


@login_required(login_url='login')
def change_password(request):
    form = ChangePasswordForm()
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        #  get all passwords as variables
        user = CustomUser.objects.get(username=request.user)
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password_repeat = request.POST.get('new_password_repeat')

        if old_password == user.password and form.is_valid() and new_password == new_password_repeat and new_password != old_password:
            print('all good')
            CustomUser.objects.filter(
                username=request.user).update(password=new_password)
            return redirect('login')
        else:
            return redirect('change_password')

    return render(request, 'Mylibrary/Register.html', {'form': form})


def user_logout(request):
    auth.logout(request)
    return redirect('login')


def search_book(request):
    books = Book.objects.all()
    myFilter = BookFilters(request.GET, queryset=books)
    books = myFilter.qs
    context = {
        'myFilter': myFilter,
        'books': books,

    }
    return render(request, 'Mylibrary/search_book.html', context)


def remove_book_from_wish_list(request, pk):

    book = Book.objects.get(id=pk)
    user = CustomUser.objects.get(username=request.user)

    object = book
    print(wishlist)
    if request.method == 'POST':
        pass
    return render(request, 'Mylibrary/delete_book.html', {'object': object})
