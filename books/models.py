from django.db import models


# Create your models here.
class Book(models.Model):
    status = [
        ("Read", "Read"),
        ("Reading", "Reading"),
        ("Want to Read", "Want to Read"),
    ]

    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=50, null=False)
    status = models.CharField(choices=status)
    date_added = models.DateField(auto_now_add=True)
    date_read = models.DateField(null=True)
