from rest_framework import viewsets, decorators, response, status

from post_statistics.models import Statistic
from post_statistics.serializers import (
    StatisticSerializer,
    StatisticCreaterSerializer,
    AverageStatisticSerializer
)
from post_statistics.utils import get_latest_statistic, get_average_statistics


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'create':
            return StatisticCreaterSerializer

        if hasattr(self, 'action') and self.action == 'average':
            return AverageStatisticSerializer

        return StatisticSerializer

    @decorators.action(methods=['GET'], detail=False)
    def post(self, request, *args, **kwargs):
        params = request.query_params
        post_id = params.get('post_id')
        latest = params.get('latest')

        if latest:
            latest = int(latest)

        queryset = self.get_queryset()
        statistics = get_latest_statistic(queryset=queryset, params={'post_id': post_id}, latest=latest)

        serializer = self.get_serializer(statistics, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @decorators.action(methods=['GET'], detail=False)
    def user(self, request):
        params = request.query_params
        user_id = params.get('user_id')
        latest = params.get('latest')

        if latest:
            latest = int(latest)

        queryset = self.get_queryset()
        statistics = get_latest_statistic(queryset=queryset, params={'user_id': user_id}, latest=latest)

        serializer = self.get_serializer(statistics, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @decorators.action(methods=['GET'], detail=True)
    def average(self, request, *args, **kwargs):
        queryset = Statistic.objects.filter(user_id=kwargs.get('pk'))

        if not queryset.exists():
            raise Statistic.DoesNotExist()

        likes_average = get_average_statistics(queryset=queryset)

        statistics = {
            'user_id': kwargs.get('pk'),
            'likes_average': likes_average
        }

        serializer = self.get_serializer(statistics)
        return response.Response(serializer.data)
