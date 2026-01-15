from django.db import models

# Create your models here.
class AppUser(models.Model):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField( upload_to='images')

    def __str__(self):
        return self.username