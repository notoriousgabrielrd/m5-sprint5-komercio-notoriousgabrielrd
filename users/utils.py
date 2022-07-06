from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,first_name,last_name,is_seller,**extra_fields):

        if not email:
            raise ValueError("O email é um campo obrigatório.")

        email = self.normalize_email(email)

        user = self.model(
            email           = email,
            first_name      = first_name,
            last_name       = last_name,
            is_superuser    = False,
            is_seller       = is_seller,
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self._db)

        return user


    # def create_user_buyer(self,email,password,first_name,last_name,**extra_fields):

    #     if not email:
    #         raise ValueError("O email é um campo obrigatório.")

    #     email = self.normalize_email(email)

    #     user = self.model(
    #         email        = email,
    #         first_name   = first_name,
    #         last_name    = last_name,
    #         is_superuser = False,
    #         is_seller    = False,
    #         **extra_fields
    #     )

    #     user.set_password(password)
    #     user.save(using = self._db)

    #     return user

    def create_superuser(self,email,password,first_name,last_name,is_seller,**extra_fields):
        
        if not email:
            raise ValueError("O email é um campo obrigatório.")

        email = self.normalize_email(email)
        
        user = self.model(
            email           = email,
            first_name      = first_name,
            last_name       = last_name,
            is_superuser    = True,
            is_seller       = is_seller,
            **extra_fields
        )

        user.set_password(using=self._db)

        return user