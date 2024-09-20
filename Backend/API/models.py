from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser): #adding more fields to the inbuilt User Model
    user_id = models.AutoField(primary_key=True) #will be the primary key, and will be unique for each user
    username = models.CharField(max_length=256, unique=True) 
    # password_hash = models.CharField(max_length=256)  #password will be stored in hashed format automatically, when user needs to sign in, the entered password will be hashed, and checked with the hashed password in the db.
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    account_deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'username' #specifies that the username fields is 'username'

    objects = UserManager()

    def __str__(self):
        return self.username
    


class Logs(models.Model):
    log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #links Logs models to the User model, and if the specific user is deleted, then the Logs for the particular user is also deleted.
    log_name = models.CharField(max_length=256, unique=True)
    algorithm_name = models.CharField(max_length=255)
    algorithm_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.log_name
    


