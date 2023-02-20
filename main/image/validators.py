from rest_framework import serializers
from PIL import Image


class ImageValidator:
    """
       Validator for uploaded images. Checks if the image format is allowed.
    """
    def __init__(self, allowed_formats=('JPEG', 'PNG'), message=None):
        """
        Initialize the validator with allowed image
        formats and a custom error message.

        :param allowed_formats: A tuple of allowed image formats.
        :param message: A custom error message to be raised on validation error.
        """
        self.allowed_formats = allowed_formats
        self.message = message

    def __call__(self, value):
        """
        Check if the uploaded image format is allowed.

        :param value: The uploaded image file.
        """
        if value:
            try:
                image = Image.open(value)
                if image.format not in self.allowed_formats:
                    raise serializers.ValidationError(
                        self.message or f"Only "
                                        f"{', '.join(self.allowed_formats)} "
                                        f"image formats are supported.")
            except IOError:
                raise serializers.ValidationError(self.message or
                                                  'Invalid image file.')

    def __repr__(self):
        """
        Return a string representation of the validator.
        """
        return f"{self.__class__.__name__}" \
               f"(allowed_formats={self.allowed_formats})"
