
# Create your models here.
from django.db import models
UNIT_KG = 'kg'
UNIT_GRAM = 'g'
UNIT_LITER = 'l'
UNIT_ML = 'ml'
UNIT_PIECE = 'pc'
UNIT_BOX = 'box'

UNIT_CHOICES = [
    (UNIT_KG, 'Kilogram'),
    (UNIT_GRAM, 'Gram'),
    (UNIT_LITER, 'Liter'),
    (UNIT_ML, 'Milliliter'),
    (UNIT_PIECE, 'Piece'),
    (UNIT_BOX, 'Box'),
]


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        default=UNIT_PIECE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name