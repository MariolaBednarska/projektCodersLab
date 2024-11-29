from django import forms
from .models import Book, BookCategory, BookRating, BookStatus

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'bookshelf', 'rate']

class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = ['name', 'description']

class BookRatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = ['book', 'category', 'rate']

class BookStatusForm(forms.ModelForm):
    class Meta:
        model = BookStatus
        fields = ['book', 'status']
