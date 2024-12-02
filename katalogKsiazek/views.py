from django.db import models
from django.db.models import Q
from django.urls import reverse

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Book, BOOKSHELF, BookCategory
from .forms import BookForm, BookCategoryForm, BookRatingForm, BookStatusForm, BookCategoryEditForm



# Widok listy książek
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# Widok szczegółów książki
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    pk_url_kwarg = 'book_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        context.update({
            'book': book,
            'status': book.bookstatus_set.last(),  # Ostatni status książki
            'categories': book.bookcategory_set.all(),
            'rating': book.rating if hasattr(book, 'rating') else None,
        })
        return context

# Widok dodawania książki
class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'add_book.html'

    def get_success_url(self):
        return reverse('book_detail', kwargs={'book_id': self.object.pk})

# Widok dodawania kategorii książki
class AddBookCategoryView(View):
    def get(self, request, *args, **kwargs):
        form = BookCategoryForm()
        return render(request, 'add_book_category.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=kwargs['book_id'])
        return render(request, 'add_book_category.html', {'form': form})

# Widok dodawania oceny do książki
class AddBookRatingView(View):
    def get(self, request, *args, **kwargs):
        form = BookRatingForm()
        return render(request, 'add_book_rating.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookRatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=kwargs['book_id'])
        return render(request, 'add_book_rating.html', {'form': form})

# Widok dodawania statusu książki
class AddBookStatusView(View):
    def get(self, request, *args, **kwargs):
        form = BookStatusForm()
        return render(request, 'add_book_status.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_detail', book_id=kwargs['book_id'])
        return render(request, 'add_book_status.html', {'form': form})

# Widok regału z półkami
class BookshelfView(View):
    def get(self, request, *args, **kwargs):
        shelves = [shelf for shelf, _ in BOOKSHELF]  # Pobiera listę półek
        return render(request, 'bookshelf.html', {'shelves': shelves})

# Widok książek na wybranej półce
class ShelfBooksView(View):
    def get(self, request, shelf_id, *args, **kwargs):
        books = Book.objects.filter(bookshelf=str(shelf_id))  # Filtruje książki dla danej półki
        return render(request, 'shelf_books.html', {'books': books, 'shelf_id': shelf_id})


class EditBookStatusView(View):
    def get(self, request, book_id, *args, **kwargs):
        # Pobierz książkę i jej aktualny status
        book = get_object_or_404(Book, pk=book_id)
        status = book.status if hasattr(book, 'status') else None  # Zakładam, że `status` to relacja z `BookStatus`
        form = BookStatusForm(instance=status)  # Jeśli status istnieje, wypełnij formularz danymi
        return render(request, 'edit_book_status.html', {'form': form, 'book': book})

    def post(self, request, book_id, *args, **kwargs):
        # Pobierz książkę
        book = get_object_or_404(Book, pk=book_id)
        # Stwórz formularz z przesłanymi danymi
        form = BookStatusForm(request.POST, instance=book.status if hasattr(book, 'status') else None)
        if form.is_valid():
            status = form.save(commit=False)
            status.book = book
            status.save()
            return redirect('book_detail', book_id=book.id)
        # Jeśli formularz jest nieprawidłowy, ponownie wyświetl formularz z błędami
        return render(request, 'edit_book_status.html', {'form': form, 'book': book})

class EditBookRatingView(View):
    def get(self, request, book_id, *args, **kwargs):
        # Pobierz książkę i jej aktualny rating
        book = get_object_or_404(Book, pk=book_id)
        rating = book.rating if hasattr(book, 'rating') else None  # Zakładam relację z `BookRating`
        form = BookRatingForm(instance=rating)  # Formularz wypełniony istniejącymi danymi
        return render(request, 'edit_book_rating.html', {'form': form, 'book': book})

    def post(self, request, book_id, *args, **kwargs):
        # Pobierz książkę
        book = get_object_or_404(Book, pk=book_id)
        # Stwórz formularz z przesłanymi danymi
        form = BookRatingForm(request.POST, instance=book.rating if hasattr(book, 'rating') else None)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.book = book
            rating.save()
            return redirect('book_detail', book_id=book.id)
        # Jeśli formularz jest niepoprawny
        return render(request, 'edit_book_rating.html', {'form': form, 'book': book})

class EditBookCategoryView(View):
    def get(self, request, book_id, *args, **kwargs):
        # Pobierz książkę i jej istniejące kategorie
        book = get_object_or_404(Book, pk=book_id)
        form = BookCategoryEditForm()  # Formularz bez danych początkowych
        categories = book.bookcategory_set.all()  # Założenie: relacja do `BookCategory`
        return render(request, 'edit_book_category.html', {'form': form, 'book': book, 'categories': categories})

    def post(self, request, book_id, *args, **kwargs):
        # Pobierz książkę
        book = get_object_or_404(Book, pk=book_id)
        # Obsługa formularza
        form = BookCategoryEditForm(request.POST)
        if form.is_valid():
            category_id = form.cleaned_data['category']
            category_name = dict(BookCategory.CATEGORY_CHOICES).get(int(category_id))
            # Dodanie lub aktualizacja kategorii
            category, _ = BookCategory.objects.get_or_create(book=book, name=category_name)
            category.save()
            return redirect('book_detail', book_id=book.id)
        # Jeśli formularz jest niepoprawny
        categories = book.bookcategory_set.all()
        return render(request, 'edit_book_category.html', {'form': form, 'book': book, 'categories': categories})

class SearchBooksView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', None)
        books = None
        if query:  # Jeśli jest wprowadzony tekst wyszukiwania
            books = Book.objects.filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(bookcategory__name__icontains=query)
            ).distinct()
        return render(request, 'search_books.html', {'books': books, 'query': query})
