from django.contrib.auth import get_user_model
# Create your views here.
from rest_framework import viewsets

from project.appname.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
