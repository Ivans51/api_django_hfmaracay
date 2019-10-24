from django.contrib.auth import get_user_model
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status

from project.appname.serializers import UserSerializer


@csrf_exempt
def delete_profile(request, pk):
    user = get_user_model().objects.get(pk=pk)
    user.is_active = False
    user.save()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.filter(is_active=True).order_by('-date_joined')
    serializer_class = UserSerializer
