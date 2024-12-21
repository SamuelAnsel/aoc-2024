import numpy as np
import heapq

input_text = open("input.txt", "r").read()
input_text = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

input_text = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

maze = np.array([list(row) for row in input_text.split("\n")])

def get_start_end(maze):
    start = np.asarray(np.where(maze == "S")).reshape(-1)
    end = np.asarray(np.where(maze == "E")).reshape(-1)
    return start, end

def dijkstra_best_path(maze, start, end):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = maze.shape
    costs = np.full((rows, cols), np.inf)
    costs[start[0], start[1]] = 0
    pq = [(0, start[0], start[1], 1, [])]  # (cost, x, y, previous direction, path)
    best_paths = []

    while pq:
        cost, x, y, prev_dir, path = heapq.heappop(pq)

        if (x, y) == tuple(end):
            if not best_paths or cost == best_paths[0][0]:
                best_paths.append((cost, path + [(x, y)]))
            elif cost < best_paths[0][0]:
                best_paths = [(cost, path + [(x, y)])]
            continue
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] != "#":
                new_cost = cost + 1

                if prev_dir is not None and prev_dir != i:
                    new_cost += 1000

                if new_cost <= costs[nx, ny]:
                    costs[nx, ny] = new_cost
                    heapq.heappush(pq, (new_cost, nx, ny, i, path + [(x, y)]))

    return best_paths

def min_cost(maze, start, end):
    if start[0] == end[0] and start[1] == end[1]:
        return 0
    
    min_row, max_row = min(start[0], end[0]), max(start[0], end[0])
    min_col, max_col = min(start[1], end[1]), max(start[1], end[1])
    sub_maze = maze[min_row:max_row + 1, min_col:max_col + 1]
    
    min_row_walls = min(np.count_nonzero(sub_maze == "#", axis=0))
    min_col_walls = min(np.count_nonzero(sub_maze == "#", axis=1))
    n_walls = max(0, min_row_walls + min_col_walls - 1)

    return 1000 * n_walls + abs(start[0] - end[0]) + abs(start[1] - end[1])

def dijkstra_all_paths(maze, start, end, best_cost):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows, cols = maze.shape

    pq = [(0, start[0], start[1], 1, [])]  # (cost, x, y, previous direction, path)
    best_paths = []

    while pq:
        cost, x, y, prev_dir, path = heapq.heappop(pq)
        pdx, pdy = directions[prev_dir]

        if (x, y) == tuple(end):
            if not best_paths or cost == best_cost:
                best_paths.append((cost, path + [(x, y)]))
            elif cost < best_cost:
                best_cost = cost
                best_paths = [(cost, path + [(x, y)])]
            continue
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx, ny] != "#":
                new_cost = cost + 1

                if prev_dir is not None and prev_dir != i:
                    new_cost += 1000

                print(i, (dx, dy), new_cost, best_cost, new_cost + min_cost(maze, (nx, ny), end), best_cost)
                if new_cost <= best_cost:
                    if new_cost + min_cost(maze, (nx, ny), end) <= best_cost:
                        heapq.heappush(pq, (new_cost, nx, ny, i, path + [(x, y)]))

    return best_paths

start, end = get_start_end(maze)

best_path = dijkstra_best_path(maze, start, end)[0]
best_cost, best_path = best_path
best_paths = dijkstra_all_paths(maze, start, end, best_cost)
positions = list()

for cost, path in best_paths:
    print(f"Cost: {cost}, Path: {path}")
    path_in_maze = maze.copy()

    for x, y in path:
        positions += [str(x) + "," + str(y)]

print(len(list(set(positions))))