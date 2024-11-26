from django.shortcuts import render, redirect
from django.views import View

from .forms import BookForm
from .models import Book, BOOKSHELF, RATE


