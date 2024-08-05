from django.db import models
from django.db import models
from django.core.validators import MinValueValidator

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nationality = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Phone(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    # brand_country = models.CharField(max_length=100)
    model = models.CharField(max_length=50,unique=True)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    screen_size = models.FloatField(validators=[MinValueValidator(0.0)])
    available = models.BooleanField()
    manufacturing_country = models.CharField(max_length=100)


    def __str__(self):
        return f'{str(self.brand)} - {str(self.id)}'
