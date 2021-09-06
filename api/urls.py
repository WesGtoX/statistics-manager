from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from post_statistics.viewsets import StatisticViewSet

router = routers.DefaultRouter()
router.register('statistic', StatisticViewSet, basename='statistic')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
