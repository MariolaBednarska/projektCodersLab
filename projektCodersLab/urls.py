"""
URL configuration for projektCodersLab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from katalogKsiazek.views import ShelfBooksView, BookshelfView
from django.urls import path
from katalogKsiazek.views import (BookDetailView,
                                  AddBookView,
                                  AddBookCategoryView,
                                  AddBookRatingView,
                                  AddBookStatusView,
                                  EditBookRatingView,
                                  EditBookStatusView,
                                  EditBookCategoryView
                                  )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookshelfView.as_view(), name='bookshelf'),  # Strona główna
    path('shelf/<int:shelf_id>/', ShelfBooksView.as_view(), name='shelf_books'),  # Książki na półce
    path('book/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
    path('book/add/', AddBookView.as_view(), name='add_book'),
    path('book/<int:book_id>/category/add/', AddBookCategoryView.as_view(), name='add_book_category'),
    path('book/<int:book_id>/rating/add/', AddBookRatingView.as_view(), name='add_book_rating'),
    path('book/<int:book_id>/status/add/', AddBookStatusView.as_view(), name='add_book_status'),
    path('book/<int:book_id>/status/edit/', EditBookStatusView.as_view(), name='edit_book_status'),
    path('book/<int:book_id>/rating/edit/', EditBookRatingView.as_view(), name='edit_book_rating'),
    path('book/<int:book_id>/category/edit/', EditBookCategoryView.as_view(), name='edit_book_category'),
]