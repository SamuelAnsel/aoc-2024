import numpy as np


input_txt = open("input.txt").read()

garden = np.asarray([list(row) for row in input_txt.split("\n")])

def get_regions(garden):
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
                dfs(i, j, region, garden[i, j])

                if len(region) > 0:
                    regions.append(region)

    return regions

def region_area(region):
    return len(region)

def region_perimeter(region):
    outside = list()

    for i, j in region:
        outside += [(x, y) for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if (x, y) not in region]

    perimeter = len(outside)

    return perimeter

def region_price(region):
    a, p = region_area(region), region_perimeter(region)
    price = a * p
    return price

regions = get_regions(garden)
price = 0

for region in regions:
    price += region_price(region)

print(price)