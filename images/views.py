from .models import Image
from .serializers import ImageSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
import os
from django.conf import settings


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.get_serializer(instance).data
        filename = data['image_url'][data['image_url'].rfind('/')+1:]

        os.remove(os.path.join(settings.MEDIA_ROOT, 'images', filename))

        return super().destroy(request, *args, **kwargs)