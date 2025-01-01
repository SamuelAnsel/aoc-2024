import numpy as np
import heapq
from collections import defaultdict


input_text = open('input.txt').read()


race_map = np.asarray([list(line) for line in input_text.split('\n')])
rows, cols = race_map.shape

def dijkstra(race_map, start, end):
    rows, cols = race_map.shape
    distances = { (i, j): float('inf') for i in range(rows) for j in range(cols) }
    distances[start] = 0
    priority_queue = [(0, start)]
    came_from = {start: None}

    while priority_queue:
        current_distance, current_cell = heapq.heappop(priority_queue)

        if current_cell == end:
            break

        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current_cell[0] + direction[0], current_cell[1] + direction[1])

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and race_map[neighbor] != '#':
                distance = current_distance + 1

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    came_from[neighbor] = current_cell

    path = []
    step = end

    while step is not None:
        path.append(step)
        step = came_from.get(step)

    path.reverse()

    return path

start = tuple(np.argwhere(race_map == 'S')[0])
end = tuple(np.argwhere(race_map == 'E')[0])

path = dijkstra(race_map, start, end)
cheat_count = 0

for l, (i, j) in enumerate(path[:-1]):
    race_map[i, j] = 'o'

    cheat_points = [(i + dx, j + dy) for dx in range(-2, 3) for dy in range(-2, 3) if abs(dx) + abs(dy) == 2]

    for x, y in cheat_points:
        if 0 <= x < rows and 0 <= y < cols and race_map[x, y] in '.E':
            new_start = (x, y)

            index = path.index(new_start)
            new_path_len = len(path) - index

            saved = len(path) - (new_path_len + 2 + l)

            # cheat_count[saved] += 1
            if saved >= 100:
                cheat_count += 1
    
print(cheat_count)