from .models import Image
from .serializers import ImageSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]
