from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    roles=(('A','Administrador'),('U','Usuario'))
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10,blank=True)
    userImage = models.ImageField(
        upload_to="users/pictures",
        blank=True,
        null=True
    )
    rol=models.CharField(max_length=1,choices=roles,default='A')
    created =models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username
