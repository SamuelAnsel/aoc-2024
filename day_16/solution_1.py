import numpy as np
import heapq

input_text = open("input.txt", "r").read()

maze = np.array([list(row) for row in input_text.split("\n")])

def get_start_end(maze):
    start = np.asarray(np.where(maze == "S")).reshape(-1)
    end = np.asarray(np.where(maze == "E")).reshape(-1)
    return start, end

def dijkstra(maze, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = maze.shape
    costs = np.full((rows, cols), np.inf)
    costs[start[0], start[1]] = 0
    pq = [(0, start[0], start[1], 1)]  # (cost, x, y, previous direction)

    while pq:
        cost, x, y, prev_dir = heapq.heappop(pq)

        if (x, y) == tuple(end):
            return cost
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] != "#":
                new_cost = cost + 1

                if prev_dir is not None and prev_dir != i:
                    new_cost += 1000

                if new_cost < costs[nx, ny]:
                    costs[nx, ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, i))

    return -1  # If no path is found

start, end = get_start_end(maze)
min_cost = dijkstra(maze, start, end)
print(min_cost)