from django.db import models

class Book(models.Model):
    bookname = models.CharField(max_length= 200)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)

    def __str__(self):
        return self.bookname

