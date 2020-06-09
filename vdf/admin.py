from django.contrib import admin
from .models import User, UserDetail, Campaign, Donation


# Register your models here.

# admin.site.register(User)
admin.site.register(UserDetail)
admin.site.register(Campaign)
admin.site.register(Donation)
