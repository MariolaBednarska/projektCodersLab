from audioop import reverse

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Book
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