from django.db import models



# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        db_table='category'
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.SmallIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='product'
    def __str__(self):
        return self.name
    