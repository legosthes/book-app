from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from datetime import datetime


# Create your views here.
def index(request):
    if request.POST:
        form = BookForm(request.POST)
        book = form.save(commit=False)
        if book.status == "Read":
            book.date_read = datetime.now()
        book.save()
        return redirect("books:index")
    else:
        books = Book.objects.all().order_by("-id")
        return render(request, "books/index.html", {"books": books})


def new(request):
    form = BookForm(request.POST)
    return render(request, "books/new.html", {"form": form})


def detail(request, id):
    book = Book.objects.get(pk=id)
    if request.POST:
        if request.POST["_method"] == "patch":
            form = BookForm(request.POST, instance=book)
            # 先暫存，如果只用book.status，那其實是舊的資料
            updated_form = form.save(commit=False)

            if updated_form.status == "Read":
                book.date_read = datetime.now()
            if updated_form.status == "Reading" or book.status == "Want to Read":
                book.date_read = None
            form.save()
            return redirect("books:detail", book.id)
        if request.POST["_method"] == "delete":
            book.delete()
            return redirect("books:index")
    else:
        return render(request, "books/detail.html", {"book": book})


def edit(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(instance=book)
    return render(request, "books/edit.html", {"book": book, "form": form})
