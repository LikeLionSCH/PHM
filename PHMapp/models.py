from django.db import models

# Create your models here.
class Order(models.Model) :
    image = models.ImageField(upload_to = 'images/')       #이미지
    name = models.CharField(max_length = 50)
    price = models.IntegerField();
    customer = models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    request = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    time = models.IntegerField()
    
    def __str__(self):
        return self.name


