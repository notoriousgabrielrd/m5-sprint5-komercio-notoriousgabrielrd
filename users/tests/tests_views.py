from rest_framework.authtoken.models import Token
from urllib import response
from rest_framework.test import APIClient, APITestCase
from users.models import User
from users.permissions import IsOwner
from users.serializer import LoginSerializer,SuperUserUpdateSerializer,UserSerializer,UserUpdateSerializer

class UserViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "biel@kenzie.com"
        cls.first_name = "gabriel"
        cls.last_name = "dourado"
        cls.password = "1234"
        

        cls.seller = { "email" : cls.email, "first_name" : cls.first_name,    "last_name" : cls.last_name, "password" : cls.password, "is_seller" : True
        }

        cls.not_seller = { "email" : cls.email, "first_name" : cls.first_name,    "last_name" : cls.last_name, "password" : cls.password, "is_seller" : False
        }
        
        cls.user = {"email": "biel@kenzie.com", "password": "1234"}


    def test_create_seller_account(self):
        response = self.client.post("/api/accounts/", data=self.seller)
        user = User.objects.get(id=1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(user.is_seller, True)
        self.assertIn("email", response.data)
        self.assertIn("id", response.data)

    def test_create_empty_fields(self):
        response = self.client.post("/api/accounts/", data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("email",response.data)
       

    def test_create_not_seller_account(self):


        response = self.client.post("/api/accounts/", data=self.not_seller)
        user = User.objects.get(id=1)
        self.assertEqual(response.status_code, 201)
        self.assertIn("email", response.data)
        self.assertIn("id", response.data)
        self.assertEqual(user.is_seller, False)


    def test_login_auth_token(self):
        new_user = User.objects.create_user(**self.seller)

        res = self.client.post("/api/login/", data=self.user)
        
        self.assertEqual(res.status_code,200)
        self.assertEqual(new_user.auth_token.key, res.data["token"])

    def test_login_invalid_credentials(self):
        res = self.client.post("/api/login/", data=self.user)

        self.assertEqual(res.status_code, 401)



    def test_list_users(self):
        users = [
            User.objects.create(email=f"gabriel{user_id}@kenzie.com", first_name = "gabriel", last_name = "dourado", password = "1234", is_seller = True) for user_id in range(1, 6)
        ]

        res = self.client.get("/api/accounts/")

        self.assertEqual(res.status_code,200)
        self.assertEqual(len(res.data),5)
