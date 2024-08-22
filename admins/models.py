from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractUser
from .cargos import select 

class MyUserManager (BaseUserManager):
    def create_user (self , email , password = None , **extra_fields ):
        if not email :
            raise ValueError ('El correo electronico es obligatorio')
        user = self.model (
            email = self.normalize_email (email),
            **extra_fields
            )
        user.set_password (password)
        user.save (using = self._db)
        return user

    def create_superuser (self, email, password = None , **extra_fields):
        user = self.create_user (
            email ,
            password = password ,
            **extra_fields
        )
        user.is_admin = True
        user.save (using = self._db)
        return user

class Myuser (AbstractUser):
    email = models.EmailField (verbose_name = 'Dirección electronico' , max_length = 255 ,unique = True)
    name = models.CharField (max_length = 25 , blank = False , null = False)
    last_name = models.CharField (max_length = 25 , blank = False , null = False)
    position = models.CharField (max_length = 65 , choices = select.cargo() , blank = False, null = False)
    username = None
    last_login = None
    first_name = None
    last_name = None
    date_joined = None

    is_active = models.BooleanField (default = True)
    is_admin = models.BooleanField (default = False)

    objects = MyUserManager ()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms (self , app_lable):
        return True

    @property
    def is_staff (self):
        return self.is_admin

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'Users'
        ordering = ['email' , '-name']
