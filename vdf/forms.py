from django import forms
from .models import *


class AddCampaignForm(forms.Form):
    name = forms.CharField(label='name', max_length=254)
    shortDescription = forms.CharField(label='description', max_length=400)
    goal = forms.IntegerField(label='money')
    expiredDate = forms.DateField(label='deadline')
    coverImage = forms.ImageField(label='coverImage')
    fullDescription = forms.CharField(label='editorContent', widget=forms.Textarea)
    ownerID = forms.CharField(label='ownerID')