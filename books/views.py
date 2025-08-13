from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book


# Create your views here.
def index(request):
    if request.POST:
        form = BookForm(request.POST)
        form.save()
        return redirect("books:index")
    else:
        books = Book.objects.all().order_by("-id")
        return render(request, "books/index.html", {"books": books})


def new(request):
    form = BookForm(request.POST)
    return render(request, "books/new.html", {"forms": form})


def detail(request, id):
    book = Book.objects.get(pk=id)
    if request.POST["_method"] == "patch":
        form = BookForm(request.POST, instance=book)
        form.save()
        return redirect("books:detail", book.id)
    else:
        return render(request, "books/detail.html", {"book": book})


def edit(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST, instance=book)
    return render(request, "books/edit.html", {"book": book, "form": form})
