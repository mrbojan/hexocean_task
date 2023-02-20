from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Account, Image
from .serializers import UploadImageSerializer, AccountSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# View for listing image
class ImageListViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


# View for upload image
class UploadImageViewSet(viewsets.ModelViewSet):
    serializer_class = UploadImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ''
