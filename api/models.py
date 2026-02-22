from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'image': self.image
        }

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    total = models.FloatField()
    products = models.CharField(max_length=2083)

    def to_json(self):
        return {
            'id': self.id,
            'customer': self.customer,
            'address': self.address,
            'total': self.total,
            'products': self.products
        }