input_txt = open('input.txt', 'r').read()

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

pebbles = list(map(int, input_txt.split()))

for i in range(25):
    pebbles = blink182(pebbles)

print(len(pebbles))