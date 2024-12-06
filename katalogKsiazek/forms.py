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

class BookCategoryEditForm(forms.Form):
    category = forms.ChoiceField(choices=BookCategory.CATEGORY_CHOICES, label="Kategoria")

class BookRatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = ['rate']
        labels = {'rate': 'Wybierz ocenę'}

class BookStatusForm(forms.ModelForm):
    class Meta:
        model = BookStatus
        fields = ['status']
        labels = {'status': 'Wybierz status'}