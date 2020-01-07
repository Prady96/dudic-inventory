from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from phone_field import PhoneField
from django.contrib.auth.models import BaseUserManager
# from image_cropping import ImageRatioField
from smart_selects.db_fields import ChainedForeignKey 


class RoleOfUser(models.Model):
    name = models.CharField(max_length = 50, default = 'null')

    def __str__(self):
        return self.name

class Categorie(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class InventoryPresent(models.Model):
    """Inventory Present in the Store """
    quantity  = models.IntegerField(default='1')
    user      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    item_name = models.CharField(max_length = 30)
    date      = models.DateField(auto_now_add = True)
    brand     = models.CharField(max_length = 30)
    category  = models.ForeignKey(Categorie, null=True ,on_delete=models.SET_NULL)

    picture   = models.ImageField(  null=True,
                                    blank = True,
                                    upload_to='inventory_thumbnails/',
                                    default = 'images/sample_image.png')

    ## size is "width x height"
    # cropping = ImageRatioField('picture', '300x300')

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural = 'Inventory Present'


class InventoryIssued(models.Model):
    """Inventory Issued to peron """

    get_user_type = models.ForeignKey(RoleOfUser, on_delete=models.CASCADE)

    user          = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     null=True, blank=True,
                                     on_delete=models.SET_NULL,
                                     )

    get_users     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'issued')

    item_name     = models.ManyToManyField(InventoryPresent)
    date          = models.DateField(auto_now_add = True)
    quantity      = models.IntegerField(default = '1')

    status        = [("APP","Approved"),
                    ("DEC","Declined"),]

    item_status   = models.CharField(choices = status, blank=False, max_length = 3)

    def __str__(self):
        return str(self.get_users)

    class Meta:
        verbose_name_plural = 'Inventory Issued'


class User_manager(BaseUserManager):
    def create_user(self, username, email, name, 
                    phone_number,password):

        email    = self.normalize_email(email)
        user     = self.model(username=username, email=email, name=name,
                            phone_number=phone_number,)

        user.is_active = True
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username, email, name, 
                        phone_number,password):

        user = self.create_user(username=username, email=email, name=name,
                                phone_number=phone_number, password=password)

        user.is_superuser = True
        user.is_staff     = True
        user.save(using=self._db)

        return user

class UserProfile(PermissionsMixin, AbstractBaseUser):

    username    = models.CharField(max_length=32, unique=True,)
    email       = models.EmailField(max_length=32, unique=True,)

    name        = models.CharField(max_length=32, blank=False,)

    user_type   = models.ForeignKey(
                    RoleOfUser, 
                    on_delete=models.CASCADE, 
                    null=True, blank=True)

    phone_number = PhoneField(unique=True,
                            blank=False,)

    date_created = models.DateField(auto_now_add = True)

    is_active    = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email","name",
                        "phone_number",]

    USERNAME_FIELD = "username"
    objects = User_manager()

    def get_full_name(self):
        """ Retrive full Name """
        return self.name

    def __str__(self):
        return str(self.username)


