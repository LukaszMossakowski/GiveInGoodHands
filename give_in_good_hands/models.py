from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from Projekt_1.settings import AUTH_USER_MODEL
from .managers import MyUserManager


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=False)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


# class MyUserManager(BaseUserManager):
#
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Użytkownik musi mieć adres email')
#
#         user=self.model(
#             email=self.normalize_email(email),
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name


class Institutions(models.Model):
    name = models.CharField(max_length=64)
    type_choice = (
        ('fundacja', 'fundacja'),
        ('organizacja_pozarządowa', 'organizacja pozarządowa'),
        ('zbiórka_lokalna', 'zbiórka lokalna'),
    )
    type = models.CharField(max_length=64, choices=type_choice, default='fundacja')
    description = models.TextField()
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Institutions"
        verbose_name_plural = "Institutions"

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.SmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.IntegerField()
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=256)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_taken_choice = (
        ('zabrane', 'zabrane'),
        ('niezabrane', 'niezabrane'),
    )
    is_taken = models.CharField(max_length=64, choices=is_taken_choice, default='niezabrane', blank=True)

    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donation"
