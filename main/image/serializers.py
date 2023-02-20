from rest_framework import serializers
from .models import Image, Account, Tier
from django.conf import settings
from .validators import ImageValidator


# Serializer for the Tier model
class TierSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    thumbnail_size = serializers.CharField(max_length=200)
    generate_expiring_links = serializers.BooleanField(default=False)
    original_links = serializers.BooleanField(default=False)

    class Meta:
        model = Tier
        fields = ('name', 'thumbnail_size', 'generate_expiring_links',
                  'original_links')


# Serializer for uploading an image
class UploadImageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # Validate image using ImageValidator
    image = serializers.ImageField(validators=[ImageValidator()])

    class Meta:
        model = Image
        fields = '__all__'


# Serializer for retrieving Account with its associated images
class AccountSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ('images',)

    # Method to retrieve images based on the account's tier
    def get_images(self, obj):
        base_url = settings.BASE_URL
        tier = obj.tier
        urls = []
        for image in obj.user.image_set.all():
            image_dict = {}
            if tier.name == 'Basic':
                # For Basic tier, only retrieve the 200x200 thumbnail
                image_dict['id'] = image.id
                image_dict['image_thumbnail_200'] = \
                    base_url + image.image_thumbnail_200.url
            elif tier.name == 'Premium':
                # For Premium tier, retrieve both 200x200 and 400x400 thumbnails
                image_dict['id'] = image.id
                image_dict['image_thumbnail_200'] = \
                    base_url + image.image_thumbnail_200.url
                image_dict['image_thumbnail_400'] = \
                    base_url + image.image_thumbnail_400.url
            elif tier.name == 'Enterprise':
                # For Enterprise tier,
                # retrieve the original image, as well as both thumbnails
                image_dict['id'] = image.id
                image_dict['oryginal_image'] = \
                    base_url + image.image.url
                image_dict['image_thumbnail_200'] = \
                    base_url + image.image_thumbnail_200.url
                image_dict['image_thumbnail_400'] = \
                    base_url + image.image_thumbnail_400.url
            # Append the image information to the URLs list
            urls.append(image_dict)
        # Return the list of image URLs
        return urls