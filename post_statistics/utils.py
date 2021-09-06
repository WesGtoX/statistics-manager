from datetime import datetime, timedelta
from typing import Dict
from django.db.models import QuerySet, Avg


def get_latest_statistic(queryset: QuerySet, params: Dict[str, str], latest: int = 10):
    return queryset.filter(**params).order_by('-created_at')[:latest:-1]


def get_average_statistics(queryset: QuerySet):
    date = datetime.now() - timedelta(days=30)
    return queryset.filter(created_at__gte=date).aggregate(Avg('likes')).get('likes__avg')
