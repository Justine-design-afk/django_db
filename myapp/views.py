from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from myapp.models import Book
from .my_forms import BookForm


def showbook(request):
    books = Book.objects.all()
    return render(request, 'showbook.html', context={'books': books})


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


def delete_books(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.error(request, f'{book.title}Deleted successfully')
    return redirect('showbook')


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
