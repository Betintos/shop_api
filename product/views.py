from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *


class PermissionMixin:
    def get_permissions(self):
        if self.action in ["retrieve", "list"]:
            permissions = [AllowAny]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]


class CategoryViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return self.serializer_class


class ProductImageView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminUser]