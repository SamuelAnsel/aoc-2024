def count_xmas_occurrences(word_search):
    def search_from_position(x, y, dx, dy):
        for i in range(4):
            if not (0 <= x + i * dx < len(word_search) and 0 <= y + i * dy < len(word_search[0])):
                return False
            if word_search[x + i * dx][y + i * dy] != "XMAS"[i]:
                return False
        return True

    directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]
    count = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            for dx, dy in directions:
                if search_from_position(i, j, dx, dy):
                    count += 1
    return count

input = open("input.txt").read()

word_search = input.split("\n")
print(count_xmas_occurrences(word_search))
