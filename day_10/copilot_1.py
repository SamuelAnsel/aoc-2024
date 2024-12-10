def parse_map(input_str):
    return [list(map(int, line)) for line in input_str.splitlines()]

def find_trailheads(map_data):
    trailheads = []
    for r, row in enumerate(map_data):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads

def is_valid_move(map_data, r, c, next_r, next_c):
    if 0 <= next_r < len(map_data) and 0 <= next_c < len(map_data[0]):
        return map_data[next_r][next_c] == map_data[r][c] + 1
    return False

def find_trails(map_data, r, c):
    if map_data[r][c] == 9:
        return 1
    trails = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_r, next_c = r + dr, dc + dc
        if is_valid_move(map_data, r, c, next_r, next_c):
            trails += find_trails(map_data, next_r, next_c)
    return trails

def calculate_trailhead_scores(map_data):
    trailheads = find_trailheads(map_data)
    total_score = 0
    for r, c in trailheads:
        total_score += find_trails(map_data, r, c)
    return total_score

def main(input_str):
    map_data = parse_map(input_str)
    return calculate_trailhead_scores(map_data)

# Example usage
input_str = open("input.txt").read()

print(main(input_str))
