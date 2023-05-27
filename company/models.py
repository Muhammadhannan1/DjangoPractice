from django.db import models
from django.core.validators import MinValueValidator,MinLengthValidator, MaxLengthValidator,FileExtensionValidator

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(validators=[MinValueValidator(100)])
    description = models.CharField(max_length=500, validators=[MinLengthValidator(10), MaxLengthValidator(500)])
    #image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    added_date = models.DateTimeField(auto_now_add=True)