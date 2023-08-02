from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PathfinderSerializer
from .algorithms import *


ALGORITHM_FUNCTIONS = {
    'Dijkstra': dijkstra_algorithm,
    'AStar': astar_algorithm,
    'bfs': bfs_algorithm,
    'dfs': dfs_algorithm
}


class PathfinderView(APIView):
    def post(self, request, format=None):
        serializer = PathfinderSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        rows = validated_data['rows']
        columns = validated_data['columns']
        obstacles = validated_data['obstacles']
        start_x = validated_data['start_x']
        start_y = validated_data['start_y']
        target_x = validated_data['target_x']
        target_y = validated_data['target_y']
        algorithm = validated_data['algorithm']

        obstacles = [(obstacle['x'], obstacle['y']) for obstacle in obstacles]

        pathfinding_algorithm = ALGORITHM_FUNCTIONS.get(algorithm)

        if pathfinding_algorithm:
            visited, path = pathfinding_algorithm(rows, columns, obstacles, start_x, start_y, target_x, target_y)
        else:
            return Response({'error': 'Invalid algorithm choice.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'visited': visited, 'path': path}, status=status.HTTP_200_OK)
