from django.db import models
from vdf.models import Campaign

campaignName = Campaign.name
campainShortD = Campaign.shortDescription
campainGoal = Campaign.goal
campainExDate = Campaign.expiredDate
# campainImage = Campaign.coverImage
campainFullD = Campaign.fullDescription

camps = Campaign.object.all()

