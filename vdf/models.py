from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length = 64)
#     password = models.CharField(max_length = 64)
#     email = models.EmailField()
#     phone = models.CharField(max_length=10)
#     def __str__(self):
#         return (self.username)
# class Posts(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=64)
#     content = models.CharField(max_length=64)
#     image = models.CharField(max_length=64)
#     money = models.FloatField()
#
#     def __str__(self):
#         return(self.author)


class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=254)
    phoneNumber = models.CharField(max_length=11)
    address = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=254)
    shortDescription = models.CharField(max_length=400)
    goal = models.IntegerField()
    expiredDate = models.DateField()
    createdDate = models.DateField(auto_now_add=True)
    coverImage = models.ImageField(upload_to='img/')
    fullDescription = models.TextField()
    ownerID = models.ForeignKey(UserDetail, on_delete=models.CASCADE)

    def get_absolute_url(self, type="detail"):
        if type == "detail":
            return reverse("project-detail", kwargs={"my_id": self.id})
        return reverse("donate-campaign", kwargs={"my_id": self.id})

    def __str__(self):
        return self.name


class Donation(models.Model):
    userID = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    campaignID = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    donationDate = models.DateField(auto_now_add=True)
    message = models.TextField()
    ammount = models.FloatField()
    method = models.CharField(max_length=200)