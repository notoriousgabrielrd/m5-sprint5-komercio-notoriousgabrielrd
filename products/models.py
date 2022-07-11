from django.db import models


class ProductsModel(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    seller = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="products")

    # 1 USER ( SELLER ) ----------- N PRODUTOS
    # 1 PRODUTO         ----------- 1 USER ( SELLER )