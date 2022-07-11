from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.email = "biel@kenzie.com"
        cls.first_name = "gabriel"
        cls.last_name = "dourado"
        cls.password = "1234"
        cls.is_seller = True

        cls.user = User.objects.create(
            email = cls.email, first_name = cls.first_name, last_name = cls.last_name, password = cls.password, is_seller = cls.is_seller
        )


    def test_email_field_unique(self):
        user = User.objects.get(id=1)
        email_unique = user._meta.get_field("email").unique
        self.assertEquals(email_unique, True)

    def test_first_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("first_name").max_length
        self.assertEquals(max_length, 50)


    def test_last_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field("last_name").max_length
        self.assertEquals(max_length, 50)

    def test_user_has_information_fields(self):
        self.assertEqual(self.user.first_name, self.first_name)
        self.assertEqual(self.user.last_name, self.last_name)
        self.assertEqual(self.user.password, self.password)
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user.is_seller, self.is_seller)



    def test_user_has_all_full_fields(self):
        self.assertEquals(self.user.email, self.email)
        self.assertEquals(self.user.first_name, self.first_name)
        self.assertEquals(self.user.last_name, self.last_name)
        self.assertEquals(self.user.password, self.password)
        self.assertEquals(self.user.is_seller, self.is_seller)