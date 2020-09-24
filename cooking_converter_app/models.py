from django.db import models
from django.core.validators import FileExtensionValidator


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    bulk_density = models.DecimalField(max_digits=4, decimal_places=3)
    category = models.CharField(max_length=100, null=True, blank=True)
    icon = models.FileField(upload_to='icons/%Y/%m',
                            validators=[FileExtensionValidator(['svg'])],
                            blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.ingredient_name
