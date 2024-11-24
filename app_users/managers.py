from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
   
    def create_user(self, email: str, first_name: str = '', last_name: str = '', password=None):
     if not email:
         raise ValueError("The Email field must be set.")

     email = self.normalize_email(email)

     if not password:
         password = "defaultpassword123"  # Default parol
     user = self.model(
         email=email,
         first_name=first_name,
         last_name=last_name,
         is_active=True,
     )
     user.set_password(password)
     user.save(using=self._db)
     return user

    
    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    


