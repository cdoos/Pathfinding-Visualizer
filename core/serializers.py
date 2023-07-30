from rest_framework import serializers
from .algorithms import ALGORITHM_CHOICES


class PointSerializer(serializers.Serializer):
    x = serializers.IntegerField(min_value=1, max_value=1000)
    y = serializers.IntegerField(min_value=1, max_value=1000)


class PathfinderSerializer(serializers.Serializer):
    rows = serializers.IntegerField(min_value=1, max_value=1000)
    columns = serializers.IntegerField(min_value=1, max_value=1000)
    obstacles = PointSerializer(many=True)
    start_x = serializers.IntegerField(min_value=1, max_value=1000)
    start_y = serializers.IntegerField(min_value=1, max_value=1000)
    target_x = serializers.IntegerField(min_value=1, max_value=1000)
    target_y = serializers.IntegerField(min_value=1, max_value=1000)
    algorithm = serializers.ChoiceField(choices=ALGORITHM_CHOICES)
