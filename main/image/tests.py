from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from PIL import Image
import tempfile


class ImageTestCase(TestCase):
    # Set up any necessary data for the tests
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    # Write a test for uploading an image
    def test_upload_image(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        response = self.client.post('/upload_image/', {'image': tmp_file})
        self.assertEqual(response.status_code, 201)

    # Write a test for listing images
    def test_list_images(self):
        response = self.client.get('/list_image/')
        self.assertEqual(response.status_code, 200)