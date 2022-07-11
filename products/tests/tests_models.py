from django.test import TestCase
from products.models import ProductsModel
from users.models import User

class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.description = "Mouse gamer novo e muito bom pra você jogar."
        cls.price = 55.50
        cls.quantity = 99
        cls.seller = User.objects.create(
            email = "gabriel@kenzie.com", first_name = "gabriel", last_name = "dourado", password = "1234", is_seller = True
        )


        cls.product = ProductsModel.objects.create(
            description = cls.description,
            price = cls.price,
            quantity = cls.quantity,
            seller = cls.seller
        )


    def test_description(self):
        product = ProductsModel.objects.get(id=1)
        product_description = product._meta.get_field("description")
        self.assertIsNotNone(product_description)


    def test_price_decimals(self):
        product = ProductsModel.objects.get(id=1)
        product_digits = product._meta.get_field("price").max_digits
        product_decimal_places = product._meta.get_field("price").decimal_places
        self.assertEquals(product_digits,10)
        self.assertEquals(product_decimal_places,2)


    def test_quantity(self):
        product = ProductsModel.objects.get(id=1)
        product_quantity = product._meta.get_field("quantity")
        self.assertIsNotNone(product_quantity)


    def test_seller(self):
        product = ProductsModel.objects.get(id=1)
        product_seller_id = product.seller_id
        seller = User.objects.get(id=1)
        self.assertEquals(product_seller_id,seller.id)


    def test_is_active(self):
        product = ProductsModel.objects.get(id=1)
        is_active_info = product._meta.get_field("is_active").default
        self.assertEquals(is_active_info,True)


    def test_product_has_all_full_fields(self):
        self.assertEquals(self.product.description, self.description)
        self.assertEquals(self.product.price, self.price)
        self.assertEquals(self.product.quantity, self.quantity)
        self.assertIsNotNone(self.product.is_active)
        self.assertEquals(self.product.seller, self.seller)


    def test_products_may_content_one_seller(self):
        self.assertIs(self.product.seller, self.seller)
