import heapq

ALGORITHM_CHOICES = [
    ('Dijkstra', 'Dijkstra'),
    ('AStar', 'A*'),
    ('bfs', 'Breadth-First Search'),
    ('dfs', 'Depth-First Search'),
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
    class Node:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.g = float('inf')
            self.h = 0
            self.f = 0
            self.parent = None

        def __lt__(self, other):
            return self.f < other.f

    def heuristic(node, goal):
        return abs(node.x - goal.x) + abs(node.y - goal.y)

    def reconstruct_path(node):
        path = []
        while node is not None:
            path.insert(0, (node.x, node.y))
            node = node.parent
        return path

    start, target = Node(start_x, start_y), Node(target_x, target_y)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    open_set = []

    if (start_x, start_y) not in obstacles:
        heapq.heappush(open_set, start)

    start.g = 0

    visited = []

    while open_set:
        current_node = heapq.heappop(open_set)
        if (current_node.x, current_node.y) == (target.x, target.y):
            return visited, reconstruct_path(current_node)

        visited.append((current_node.x, current_node.y))

        for dx, dy in directions:
            next_x, next_y = current_node.x + dx, current_node.y + dy

            if 1 <= next_x <= rows and 1 <= next_y <= columns and (next_x, next_y) not in obstacles:
                next_node = Node(next_x, next_y)
                tentative_g = current_node.g + 1

                if tentative_g < next_node.g:
                    next_node.g = tentative_g
                    next_node.h = heuristic(next_node, target)
                    next_node.f = next_node.g + next_node.h
                    next_node.parent = current_node
                    if (next_node.x, next_node.y) not in visited:
                        heapq.heappush(open_set, next_node)

    return visited, []


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


def dfs_algorithm(rows, columns, obstacles, start_x, start_y, target_x, target_y):
    starting_node = (start_x, start_y)

    stack, visited_in_order = [], []
    visited = [[False for _ in range(columns + 1)] for _ in range(rows + 1)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    path = []

    def dfs_recursive(row, col):
        if not (1 <= row <= rows and 1 <= col <= columns and (row, col) not in obstacles) or visited[row][col]:
            return False

        visited[row][col] = True
        visited_in_order.append((row, col))

        path.append((row, col))

        if (row, col) == (target_x, target_y):
            return True

        for dr, dc in directions:
            if dfs_recursive(row + dr, col + dc):
                return True

        path.pop()
        return False

    dfs_recursive(start_x, start_y)

    return visited_in_order, path
