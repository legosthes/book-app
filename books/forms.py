from .models import Book
from django.forms import ModelForm, TextInput, Select


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "status"]
        labels = {"title": "Title", "author": "Author", "status": "Reading Status"}
        widgets = {
            "title": TextInput,
            "author": TextInput,
            "status": Select,
        }
