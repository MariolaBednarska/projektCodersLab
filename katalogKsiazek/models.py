from django.db import models

# Create your models here.
class Book(models.Model):
    class BookStatus(models.TextChoices):
        AVAILABLE = 'available', _('Available')
        BORROWED = 'borrowed', _('Borrowed')
        RESERVED = 'reserved', _('Reserved')
        UNAVAILABLE = 'unavailable', _('Unavailable')

    title = models.CharField(max_length=255, verbose_name="Title")
    author = models.CharField(max_length=255, verbose_name="Author")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    publisher = models.CharField(max_length=255, verbose_name="Publisher", blank=True, null=True)
    publication_year = models.PositiveIntegerField(verbose_name="Year of Publication", blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=BookStatus.choices,
        default=BookStatus.AVAILABLE,
        verbose_name="Status"
    )
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Added")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["-added_at"]