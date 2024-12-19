from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import GroupSerializer


@api_view()
def hello_world_view(request: Request) -> Response:
    return Response({"message": "Hello World!"})  # Исправлено: "messege" → "message"


class GroupsListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]  # Ограничен доступ только для аутентифицированных пользователей



