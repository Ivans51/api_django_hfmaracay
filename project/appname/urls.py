from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from project.appname.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
]

urlpatterns += router.urls
