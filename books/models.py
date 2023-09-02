from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def book_image_path(instance, filename):
    return f'books/{instance.id}/{filename}'

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books_owned')
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to=book_image_path)
    requested_exchanges = models.ManyToManyField('self', through='ExchangeRequest', symmetrical=False, related_name='exchanges_requested_by')
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class ExchangeRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exchange_requests')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='exchange_requests')
    book_to_exchange = models.ForeignKey(Book, on_delete=models.CASCADE, default=None)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Solicitud de {self.requester.username} para intercambiar {self.book_to_exchange.title}"


class Trade(models.Model):
    from_user = models.ForeignKey(User, related_name='trades_offered', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='trades_received', on_delete=models.CASCADE)
    book_offered = models.ForeignKey(Book, related_name='trade_offered', on_delete=models.CASCADE)
    book_desired = models.ForeignKey(Book, related_name='trade_desired', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

