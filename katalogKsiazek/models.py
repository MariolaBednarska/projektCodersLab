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
    bookshelf = models.IntegerField(choices=BOOKSHELF, default=1)
    rate = models.IntegerField(default=0)

    @property
    def name(self):
        return "{} {}".format(self.title, self.author)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    CATEGORY_CHOICES = (
        (1, "Fantastyka"),
        (2, "Literatura piękna polska"),
        (3, "Literatura piękna obca"),
        (4, "Obyczaj"),
        (5, "Reportaż"),
        (6, "Kryminał"),
        (7, "Biografie"),
        (8, "Historia"),
        (9, "Sensacja"),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    rate = models.IntegerField(choices=RATE)

    def __str__(self):
        return dict(RATE).get(self.rate, 'Brak oceny')


class BookStatus(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='statuses')
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return dict(STATUS).get(self.status, 'Nieznany status')  # Czytelne wyświetlanie statusu


class Borrower(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='borrower')
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"