from rest_framework.test import APIClient, APITestCase
from products.models import ProductsModel
from products.serializer import PostProductsSerializer,GetProductsSerializer
from users.models import User
from rest_framework.authtoken.models import Token


class ProducsViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
     
        cls.seller = User.objects.create(
            email = 'gabriel1@kenzie.com', first_name = "gabriel", last_name = "dourado", password = "1234", is_seller = True)
         
        cls.token = Token.objects.create(user = cls.seller)



    def test_only_seller_can_create_product(self):
        # seller = User.objects.create(
        #     email = f'gabriel1@kenzie.com', first_name = "gabriel", last_name = "dourado", password = "1234", is_seller = True
        #     )
        
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        user = User.objects.get(id=1)

        if self.seller.is_seller == True:
            product = {"description" : 'Product1',"price" : "10", "quantity" : "99",
            "seller" : "1"}

            res = self.client.post("/api/products/",data = product)

         
        self.assertEqual(res.status_code, 201)
        self.assertEqual(user.is_seller, True)

    def test_owner_can_update(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        user = User.objects.get(id=1)


        if self.seller == self.token.user:
            product = ProductsModel.objects.create(
            description = 'Product1',price = "10", quantity = "9",
            seller = self.seller
            )
            
            print(product)
            res = self.client.patch("/api/products/1/",data = {"description" : 'Product1',"price" : "10", "quantity" : "9",
            "seller" : "1"})

        self.assertEqual(res.status_code, 200)


    def test_create_negative_quantity(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        user = User.objects.get(id=1)

        if self.seller.is_seller == True:
            product = {"description" : 'Product1',"price" : "10", "quantity" : "-99",
            "seller" : "1"}

            res = self.client.post("/api/products/",data = product)


        self.assertEqual(res.status_code, 400)
         




    def test_update_empty_fields(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        res = self.client.patch("/api/products/1/",data = {})
        self.assertEqual(res.status_code, 404)
       


    def test_can_list_all_products(self):
        res = self.client.get("/api/products/")
        self.assertEqual(res.status_code, 200)

        
       