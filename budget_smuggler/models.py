from django.conf import settings
from django.db import models


class Expense(models.Model):
    date = models.DateTimeField()
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    item = models.TextField()
    location = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='expenses',
        on_delete=models.CASCADE)
