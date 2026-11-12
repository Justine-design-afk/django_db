from django.shortcuts import render, redirect

from myapp.models import Book
from .my_forms import BookForm




def showbook(request):
    books = Book.objects.all()
    return render(request, 'showbook.html',context={'books':books})


def addbooks(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showbook')
    else:
        form=BookForm()

    return render(request, 'addbooks.html', {'form':form})
