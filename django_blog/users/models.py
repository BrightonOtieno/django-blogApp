from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    bio = models.TextField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hobby = models.CharField( max_length=150,null=True)
    image = models.ImageField(upload_to='profile_pics',default='default.jpg')



    def __str__(self):
        return f"{self.user.username}'s Profile"
    

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

