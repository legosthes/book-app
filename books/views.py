from django.shortcuts import render
from .forms import BookForm


# Create your views here.
def index(request):
    return render(request, "books/index.html")


def new(request):
    form = BookForm()
    return render(request, "books/new.html", {"forms": form})
