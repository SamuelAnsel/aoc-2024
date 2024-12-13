from collections import defaultdict, deque

input_txt = open('input.txt', 'r').read()

cache = defaultdict(dict)
queue = deque()
pebble_count = 0
n_iterations = 75
ahead_iterations = 40

def blink182(pebbles):
    new_pebbles = []

    for pebble in pebbles:
        pebble_str = str(pebble)
        n_digits = len(pebble_str)

        if pebble == 0:
            new_pebbles += [1]
        elif n_digits % 2 == 0:
            p1, p2 = pebble_str[:n_digits // 2], pebble_str[n_digits // 2:]
            new_pebbles += [int(p1), int(p2)]
        else:
            new_pebbles += [2024 * pebble]

    return new_pebbles

pebbles = [(x, n_iterations) for x in list(map(int, input_txt.split()))]
for pebble in pebbles:
    queue.append(pebble)

while len(queue) > 0:
    pebble, remaining_iter = queue.popleft()

    if pebble in cache and remaining_iter in cache[pebble]:
        pebble_count += cache[pebble][remaining_iter]
        continue
    else:
        n_iter = min(ahead_iterations, remaining_iter)
        pebbles = [pebble]

        for i in range(n_iter):
            pebbles = blink182(pebbles)
            cache[pebble][i + 1] = len(pebbles)

        remaining_iter -= n_iter

        if remaining_iter == 0:
            pebble_count += len(pebbles)
        else:
            new_pebbles = [(x, remaining_iter) for x in pebbles]

            for pebble in new_pebbles:
                queue.append(pebble)
    
print(pebble_count)