from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# model representing the different tiers of accounts
class Tier(models.Model):
    name = models.CharField(max_length=100)
    thumbnail_size = models.CharField(max_length=200)
    generate_expiring_links = models.BooleanField(default=False)
    original_links = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# model representing a user account
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)


# model representing an uploaded image
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    image_thumbnail_200 = ImageSpecField(source='image',
                                         processors=[ResizeToFill(200, 200)],
                                         options={'quality': 60})
    image_thumbnail_400 = ImageSpecField(source='image',
                                         processors=[ResizeToFill(400, 400)],
                                         options={'quality': 60})
    def __str__(self):
        return self.image.name