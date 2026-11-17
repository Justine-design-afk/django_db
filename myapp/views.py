from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import Book
from .my_forms import BookForm, RegisterForm


@login_required
def showbook(request):
    books = Book.objects.all()
    return render(request, 'showbook.html', context={'books': books})


@login_required
@permission_required('myapp.add_books')
def addbooks(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book{request.POST.get("title")} created')

            return redirect('showbook')
    else:
        form = BookForm()

    return render(request, 'addbooks.html', {'form': form})


@login_required
@permission_required('myapp.delete_books', raise_exception=True)
def delete_books(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.error(request, f'{book.title}Deleted successfully')
    return redirect('showbook')


@login_required
def edit_books(request, id):
    books = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=books)
        if form.is_valid():
            form.save()
            messages.success(request, '{book.title} Updated Successfully')
            return redirect('showbook')

    else:
        form = BookForm(instance=books)

    return render(request, 'edit_books.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return redirect('showbook')
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', context={'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('showbook')
    else:
        form = RegisterForm()
        return render(request, 'registration/signup.html', context={'form': form})

    return none


@login_required
def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')
