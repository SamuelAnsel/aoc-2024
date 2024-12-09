import copy


input_text = open("input.txt").read()

disk_map = [int(x) for x in input_text.strip()]

def convert_to_blocks(disk_map):
    blocks = []
    
    for i, j in enumerate(range(0, len(disk_map), 2)):
        n_files = disk_map[j]

        if j + 1 < len(disk_map):
            n_free = disk_map[j + 1]

        blocks += n_files * [i] + n_free * ['.']

    return blocks

def compact_files(blocks):
    new_blocks = copy.deepcopy(blocks)
    free_idx = [i for i, b in enumerate(blocks) if b == '.'][::-1]

    for i in range(len(new_blocks) - len(free_idx), len(new_blocks))[::-1]:
        if new_blocks[i] != '.':
            new_blocks[free_idx.pop()] = new_blocks[i]
            new_blocks[i] = '.'

        if free_idx == []:
            break
    
    return new_blocks

def checksum(blocks):
    return sum([i * b for i, b in enumerate(blocks) if b != '.'])

blocks = convert_to_blocks(disk_map)
blocks = compact_files(blocks)
print(checksum(blocks))