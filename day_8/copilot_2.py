def parse_input(input_str):
    grid = input_str.strip().split('\n')
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((x, y))
    return grid, antennas

def find_antinodes(grid, antennas):
    antinodes = set()
    for freq, positions in antennas.items():
        for i, (x1, y1) in enumerate(positions):
            for j, (x2, y2) in enumerate(positions):
                if i != j:
                    if x1 == x2:  # vertical alignment
                        for y in range(min(y1, y2) + 1, max(y1, y2)):
                            antinodes.add((x1, y))
                    elif y1 == y2:  # horizontal alignment
                        for x in range(min(x1, x2) + 1, max(x1, x2)):
                            antinodes.add((x, y1))
        antinodes.update(positions)  # each antenna is also an antinode
    return antinodes

def count_unique_antinode_locations(input_str):
    grid, antennas = parse_input(input_str)
    antinodes = find_antinodes(grid, antennas)
    return len(antinodes)

# Example usage
input_str = open("input.txt").read()
print(count_unique_antinode_locations(input_str))
