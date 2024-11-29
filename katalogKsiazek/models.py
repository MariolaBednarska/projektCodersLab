from django.db import models

# Create your models here.
BOOKSHELF = (
    (1, "Półka 1"),
    (2, "Półka 2"),
    (3, "Półka 3"),
    (4, "Półka 4"),
    (5, "Półka 5"),
    (6, "Półka 6"),
    (7, "Półka 7"),
)


RATE = (
    (0, "brak oceny"),
    (1, "1 gwiazdka"),
    (2, "2 gwiazdki"),
    (3, "3 gwiazdki"),
    (4, "4 gwiazdki"),
    (5, "5 gwiazdki"),
)

STATUS = (
    ('unread', 'Nieprzeczytana'),
    ('reading', 'W trakcie czytania'),
    ('read', 'Przeczytana'),
    ('borrowed', 'Wypożyczona'),
)

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    publication_year = models.IntegerField(null=True, blank=True)
    bookshelf = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)

    @property
    def name(self):
        return "{} {}".format(self.title, self.author)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATE)


class BookStatus(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS)
