from rest_framework import serializers
from post_statistics.models import Statistic


class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = ('post_id', 'user_id', 'likes')


class StatisticCreaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = ('post_id', 'user_id', 'likes', 'created_at')


class AverageStatisticSerializer(serializers.ModelSerializer):
    likes_average = serializers.SerializerMethodField()

    def get_likes_average(self, obj):
        return obj.get('likes_average')

    class Meta:
        model = Statistic
        fields = ('user_id', 'likes_average')
