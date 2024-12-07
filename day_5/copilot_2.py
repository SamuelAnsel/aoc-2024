def parse_input(input):
    rules_section, updates_section = input.strip().split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates_section.split('\n')]
    return rules, updates

def is_correct_order(update, rules):
    for x, y in rules:
        if x in update and y in update and update.index(x) > update.index(y):
            return False
    return True

def reorder_update(update, rules):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in update if in_degree[node] == 0])
    ordered_update = []

    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ordered_update

def middle_page_number(update):
    return update[len(update) // 2]

def solve(input):
    rules, updates = parse_input(input)
    correct_updates = [update for update in updates if is_correct_order(update, rules)]
    incorrect_updates = [update for update in updates if not is_correct_order(update, rules)]

    correct_middle_sum = sum(middle_page_number(update) for update in correct_updates)
    reordered_middle_sum = sum(middle_page_number(reorder_update(update, rules)) for update in incorrect_updates)

    return correct_middle_sum, reordered_middle_sum

input = open("input.txt").read()

correct_middle_sum, reordered_middle_sum = solve(input)
print(f"Sum of middle page numbers for correctly ordered updates: {correct_middle_sum}")
print(f"Sum of middle page numbers for reordered incorrect updates: {reordered_middle_sum}")
