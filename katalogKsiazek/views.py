from audioop import reverse

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Book, BOOKSHELF
from .forms import BookForm, BookCategoryForm, BookRatingForm, BookStatusForm

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
        context['status_form'] = BookStatusForm(initial={'book': self.object})
        context['rating_form'] = BookRatingForm(initial={'book': self.object})
        context['categories'] = self.object.bookcategory_set.all()  # Wszystkie kategorie
        context['ratings'] = self.object.bookrating_set.all()  # Wszystkie oceny
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
    def post(self, request, book_id, *args, **kwargs):
        book = Book.objects.get(pk=book_id)
        form = BookStatusForm(request.POST)
        if form.is_valid():
            status = form.save(commit=False)
            status.book = book
            status.save()
        return redirect('book_detail', book_id=book.id)

class EditBookRatingView(View):
    def post(self, request, book_id, *args, **kwargs):
        book = Book.objects.get(pk=book_id)
        form = BookRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.book = book
            rating.save()
        return redirect('book_detail', book_id=book.id)
