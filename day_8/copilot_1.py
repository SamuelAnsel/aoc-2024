def parse_input(input_str):
    return [list(line) for line in input_str.strip().split('\n')]

def find_antennas(grid):
    antennas = {}
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '.':
                if cell not in antennas:
                    antennas[cell] = []
                antennas[cell].append((r, c))
    return antennas

def calculate_antinodes(grid, antennas):
    antinodes = set()
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]
                if r1 == r2:
                    dist = abs(c2 - c1)
                    if dist % 2 == 0:
                        mid = (c1 + c2) // 2
                        antinodes.add((r1, mid - dist // 2))
                        antinodes.add((r1, mid + dist // 2))
                elif c1 == c2:
                    dist = abs(r2 - r1)
                    if dist % 2 == 0:
                        mid = (r1 + r2) // 2
                        antinodes.add((mid - dist // 2, c1))
                        antinodes.add((mid + dist // 2, c1))
    return antinodes

def count_unique_antinodes(input_str):
    grid = parse_input(input_str)
    antennas = find_antennas(grid)
    antinodes = calculate_antinodes(grid, antennas)
    return len(antinodes)

# Example usage
input_str = open("input.txt").read()
print(count_unique_antinodes(input_str))
