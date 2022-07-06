from django.db import models

# Create your models here.
 
 # 1 USER ------------------ N PRODUTOS     
 #                          ForeignKey referenciando os products para a tabela USER
class ProductsModel(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    user = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="products")