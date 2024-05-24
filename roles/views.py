from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Role
from .serializers import RoleSerializer, RoleFormSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = RoleSerializer

    def list(self, request, *args, **kwargs):
        queryset = Role.objects.exclude(id=2).order_by('id')
        serializer = RoleFormSerializer(queryset, many=True)
        return Response(serializer.data)
