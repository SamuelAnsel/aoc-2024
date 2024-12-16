import numpy as np


input_txt = open("input.txt").read()
input_txt = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""
garden = np.asarray([list(row) for row in input_txt.split("\n")])

def get_regions(garden, forced_char=None):
    regions = []
    visited = np.zeros(garden.shape, dtype=bool)
    n_rows, n_cols = garden.shape

    def dfs(i, j, region, char):
        if i < 0 or i >= n_rows or j < 0 or j >= n_cols or garden[i, j] != char or visited[i, j]:
            return

        visited[i, j] = True
        region.append((i, j))

        dfs(i + 1, j, region, char)
        dfs(i - 1, j, region, char)
        dfs(i, j + 1, region, char)
        dfs(i, j - 1, region, char)

    for i in range(n_rows):
        for j in range(n_cols):
            if not visited[i, j]:
                region = []
                
                if forced_char is not None and garden[i, j] != forced_char:
                    continue

                dfs(i, j, region, garden[i, j])

                if len(region) > 0:
                    regions.append(region)

    return regions

def region_area(region):
    return len(region)

def region_sides(region):
    outside = list()

    for i, j in region:
        outside += [(x, y) for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if (x, y) not in region]

    outside = list(set(outside))
    side_map = np.zeros((garden.shape[0] + 2, garden.shape[0] + 2), dtype=str)

    for x, y in outside:
        side_map[x + 1, y + 1] = 'X'

    sides = get_regions(side_map, 'X')
    side_count = 0

    for side in sides:
        dir_count = dict({k: [] for k in [(1, 0), (-1, 0), (0, 1), (0, -1)]})

        for i, j in side:
            for dir in dir_count.keys():
                if (i + dir[0] - 1, j + dir[1] - 1) in region:
                    dir_count[dir] += [abs(i * dir[0] + j * dir[1])]

        side_count += sum([len(set(x)) for x in dir_count.values()])

    return side_count

def region_price(region):
    a, p = region_area(region), region_sides(region)
    price = a * p
    print(a, p, price, garden[region[0][0], region[0][1]])
    return price

regions = get_regions(garden)
price = 0

for region in regions:
    price += region_price(region)

print(price)