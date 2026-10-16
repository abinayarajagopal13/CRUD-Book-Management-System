from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price']
        )
        return redirect('book_list')

    books = Book.objects.all()
    return render(request, 'books_list.html',
                  {'books': books})


def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.price = request.POST['price']
        book.save()
        return redirect('books_list')

    return render(request, 'update_book.html',
                  {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books_list') 
