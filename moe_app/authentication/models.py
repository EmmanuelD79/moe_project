from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from company.models import Company
from assets.InfoBase import ContactInfo, DateTimeInfo, PhoneInfo, AddressInfo, Owner
from django.conf import settings

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser, PhoneInfo, AddressInfo, DateTimeInfo, ContactInfo):

    email = models.EmailField("Email", max_length=256, blank=False, unique=True)
    first_name = models.CharField("Prénom", max_length=256, blank=False)
    last_name = models.CharField("Nom", max_length=256, blank=False)
    user_company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Société", blank=True, null=True, related_name="user_company")
    username = None
    is_guest = models.BooleanField(default=False, verbose_name="invité")
    is_staff = models.BooleanField(default=True, verbose_name="utilisateur")
    is_superuser = models.BooleanField(default=False, verbose_name="Administrateur")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = UserManager()
    
    class Meta:
        verbose_name = "Utilisateur"
        ordering = ('email',)

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email}"


class Contact(DateTimeInfo, PhoneInfo, AddressInfo, ContactInfo, Owner):
    
    first_name = models.CharField("Prénom", max_length=256, blank=False)
    last_name = models.CharField("Nom", max_length=256, blank=False)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Société", blank=True, null=True, related_name="contact_company")
    sub_type = models.CharField("type", max_length=100, blank=True)
    is_private = models.BooleanField(default=False, verbose_name="Privé")
    
    class Meta:
        verbose_name = "Contact"
        ordering = ('pk',)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "
