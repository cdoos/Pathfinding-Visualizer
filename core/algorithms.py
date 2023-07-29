import heapq

ALGORITHM_CHOICES = [
    ('dijkstra', 'Dijkstra'),
    ('astar', 'A*'),
    ('bfs', 'Breadth-First Search'),
]


def dijkstra_algorithm(rows, columns, obstacles, start_x, start_y, target_x, target_y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    max_size = rows * columns

    distance = [[int(max_size) for _ in range(columns + 1)] for _ in range(rows + 1)]
    visited = [[False for _ in range(columns + 1)] for _ in range(rows + 1)]
    parent = [[None for _ in range(columns + 1)] for _ in range(rows + 1)]

    visualize_visited = []

    distance[start_x][start_y] = 0

    pq = [(0, (start_x, start_y))]

    path_found = False

    while pq:
        dist, current_node = heapq.heappop(pq)
        current_x, current_y = current_node

        if current_node == (target_x, target_y):
            path_found = True
            break

        if visited[current_x][current_y]:
            continue

        visited[current_x][current_y] = True

        visualize_visited.append((current_x, current_y))

        for dx, dy in directions:
            next_x, next_y = current_x + dx, current_y + dy

            if 1 <= next_x <= rows and 1 <= next_y <= columns and (next_x, next_y) not in obstacles:
                next_distance = distance[current_x][current_y] + 1

                if next_distance < distance[next_x][next_y]:
                    distance[next_x][next_y] = next_distance
                    parent[next_x][next_y] = (current_x, current_y)
                    heapq.heappush(pq, (next_distance, (next_x, next_y)))

    path = []

    if path_found:
        current_node = (target_x, target_y)

        while current_node != (start_x, start_y):
            path.append(current_node)
            current_node = parent[current_node[0]][current_node[1]]
        path.append((start_x, start_y))
        path.reverse()

    return visualize_visited, path


def astar_algorithm(rows, columns, obstacles, start_x, start_y, target_x, target_y):
    #TODO cdos
    pass


def bfs_algorithm(rows, columns, obstacles, start_x, start_y, target_x, target_y):
    starting_node = (start_x, start_y)

    queue = []
    visited = {}

    if starting_node not in obstacles:
        queue.append(starting_node)
        visited[starting_node] = None

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    path_found = False

    while queue:
        current_x, current_y = queue.pop(0)

        if current_x == target_x and current_y == target_y:
            path_found = True
            break

        for dx, dy in directions:
            next_x, next_y = current_x + dx, current_y + dy

            if 1 <= next_x <= rows and 1 <= next_y <= columns and (next_x, next_y) not in obstacles:
                if (next_x, next_y) not in visited:
                    visited[(next_x, next_y)] = (current_x, current_y)
                    queue.append((next_x, next_y))

    path = []
    current_node = (target_x, target_y)

    if path_found:
        while current_node:
            path.append(current_node)
            current_node = visited[current_node]

    path.reverse()

    return list(visited.keys()), path
