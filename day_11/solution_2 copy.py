from multiprocessing import Pool
import tqdm

N_WORKERS = 11

input_txt = open('input.txt', 'r').read()
cache = dict()

def blink182(pebbles, cache=cache):
    new_pebbles = []

    for pebble in pebbles:
        if pebble in cache:
            new_pebbles += cache[pebble]
            continue

        pebble_str = str(pebble)
        n_digits = len(pebble_str)
        next_pebble = None

        if pebble == 0:
            next_pebble = [1]
        elif n_digits % 2 == 0:
            half = n_digits // 2
            p1, p2 = pebble_str[:half], pebble_str[half:]
            next_pebble = [int(p1), int(p2)]
        else:
            next_pebble = [2024 * pebble]

        new_pebbles += next_pebble
        cache[pebble] = next_pebble
        

    return new_pebbles, cache

pebbles = list(map(int, input_txt.split()))
N = 75

with Pool(N_WORKERS) as p, tqdm.tqdm(total=N) as pbar:
    for i in range(N):
        step = len(pebbles) // N_WORKERS

        split_pebbles = [pebbles[j * step:j * step + step] for j in range(N_WORKERS - 1)] + [pebbles[(N_WORKERS - 1) * step:]]

        new_pebbles = []
        for result in p.map(blink182, split_pebbles):
            result, cache = result
            new_pebbles += result

        pebbles = new_pebbles.copy()
        pbar.update(1)

print(cache)
print(len(pebbles))