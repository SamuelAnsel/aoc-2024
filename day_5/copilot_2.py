def count_x_mas(word_search):
    rows = word_search.strip().split('\n')
    n = len(rows)
    m = len(rows[0])
    count = 0

    def check_x_mas(i, j):
        patterns = [
            [(0, 0), (1, -1), (1, 1), (2, -2), (2, 2)],  # MAS in X shape
            [(0, 0), (1, 1), (1, -1), (2, 2), (2, -2)],  # MAS in X shape reversed
        ]
        for pattern in patterns:
            if all(0 <= i + di < n and 0 <= j + dj < m and rows[i + di][j + dj] == 'M' for di, dj in pattern[:1]) and \
               all(0 <= i + di < n and 0 <= j + dj < m and rows[i + di][j + dj] == 'A' for di, dj in pattern[1:2]) and \
               all(0 <= i + di < n and 0 <= j + dj < m and rows[i + di][j + dj] == 'S' for di, dj in pattern[2:]):
                return True
        return False

    for i in range(n - 2):
        for j in range(2, m - 2):
            if check_x_mas(i, j):
                count += 1

    return count

# Example usage
input_data = open("input.txt").read()

print(count_x_mas(input_data))  # Output: 9
