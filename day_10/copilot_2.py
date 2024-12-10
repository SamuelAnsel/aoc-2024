def parse_map(input_str):
    return [list(map(int, line)) for line in input_str.strip().split('\n')]

def find_trailheads(map_data):
    trailheads = []
    for i, row in enumerate(map_data):
        for j, height in enumerate(row):
            if height == 0:
                trailheads.append((i, j))
    return trailheads

def is_valid_move(map_data, x, y, next_x, next_y):
    if 0 <= next_x < len(map_data) and 0 <= next_y < len(map_data[0]):
        return map_data[next_x][next_y] == map_data[x][y] + 1
    return False

def count_distinct_trails(map_data, x, y, memo):
    if map_data[x][y] == 9:
        return 1
    if (x, y) in memo:
        return memo[(x, y)]
    
    total_trails = 0
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_x, next_y = x + dx, y + dy
        if is_valid_move(map_data, x, y, next_x, next_y):
            total_trails += count_distinct_trails(map_data, next_x, next_y, memo)
    
    memo[(x, y)] = total_trails
    return total_trails

def sum_of_trailhead_ratings(input_str):
    map_data = parse_map(input_str)
    trailheads = find_trailheads(map_data)
    total_rating = 0
    memo = {}
    
    for x, y in trailheads:
        total_rating += count_distinct_trails(map_data, x, y, memo)
    
    return total_rating

# Example usage
input_str = open("input.txt").read()

print(sum_of_trailhead_ratings(input_str))  # Output: 81
