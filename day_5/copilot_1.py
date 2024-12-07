def parse_input(input):
    rules_section, updates_section = input.strip().split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_section.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates_section.split('\n')]
    return rules, updates

def is_correct_order(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def main(input):
    rules, updates = parse_input(input)
    correct_updates = [update for update in updates if is_correct_order(update, rules)]
    middle_pages_sum = sum(find_middle_page(update) for update in correct_updates)
    return middle_pages_sum

# Example usage
input = open("input.txt").read()

print(main(input))
