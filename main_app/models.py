from audioop import reverse
# from email.mime import image
# from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    country =models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Post(models.Model):
    title =models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    city =models.ForeignKey(City, on_delete=models.CASCADE)
    img = models.TextField(max_length=500, blank =True)
    body = models.TextField(max_length=300)
    # profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Profile(models.Model):
    title = models.CharField(max_length=50)
    email = models.CharField(max_length=300, unique=True)
    current_city = models.CharField(max_length=50)
    profile_picture =models.TextField(max_length=500, default ='https://i.pinimg.com/736x/cb/45/72/cb4572f19ab7505d552206ed5dfb3739.jpg')
    
    def get_absolute_url(self):
        return reverse('profile_detail', args=(str(self.id)))
    
    class Meta:
        ordering = ['-created_on']