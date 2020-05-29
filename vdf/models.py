from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    def __str__(self):
        return (self.username)
class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=64)
    image = models.CharField(max_length=64)
    money = models.FloatField()
    
    def __str__(self):
        return(self.author)