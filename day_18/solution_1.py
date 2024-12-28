import numpy as np
import heapq


SIZE = 71
STEPS = 1024

input_text = open('input.txt').read()

corrupted_cells = np.asarray([tuple(map(int, line.split(','))) for line in input_text.split('\n')[:STEPS]])
memory_map = np.zeros((SIZE, SIZE), dtype=int)

for x, y in corrupted_cells:
    memory_map[y, x] = 2


def dijkstra(memory_map, start, end):
    rows, cols = memory_map.shape
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

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and memory_map[neighbor] != 2:
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

start = (0, 0)
end = (SIZE-1, SIZE-1)
path = dijkstra(memory_map, start, end)

print(len(path) - 1)
