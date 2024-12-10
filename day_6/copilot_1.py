def predict_guard_path(input_map):
    directions = ['^', '>', 'v', '<']
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    guard_pos = None
    guard_dir = None
    visited = set()
    
    # Parse the input map to find the guard's initial position and direction
    map_lines = input_map.strip().split('\n')
    for r, line in enumerate(map_lines):
        for c, char in enumerate(line):
            if char in directions:
                guard_pos = (r, c)
                guard_dir = directions.index(char)
                break
        if guard_pos:
            break
    
    # Function to check if the next position is within bounds and not an obstacle
    def is_valid_move(pos):
        r, c = pos
        return 0 <= r < len(map_lines) and 0 <= c < len(map_lines[0]) and map_lines[r][c] != '#'
    
    # Simulate the guard's movement
    while True:
        visited.add(guard_pos)
        next_pos = (guard_pos[0] + moves[guard_dir][0], guard_pos[1] + moves[guard_dir][1])
        
        if not is_valid_move(next_pos):
            guard_dir = (guard_dir + 1) % 4  # Turn right
        else:
            guard_pos = next_pos
        
        # Check if the guard has left the map
        if not (0 <= guard_pos[0] < len(map_lines) and 0 <= guard_pos[1] < len(map_lines[0])):
            break
    
    return len(visited)

# Example usage
input_map = open("input.txt").read()
print(predict_guard_path(input_map))
