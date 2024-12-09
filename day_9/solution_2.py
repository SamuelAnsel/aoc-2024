import copy


input_text = open("input.txt").read()
# input_text = """2333133121414131402"""

disk_map = [int(x) for x in input_text.strip()]

def convert_to_blocks(disk_map):
    blocks = []
    files_map = []
    free_map = []
    offset = 0

    for i, j in enumerate(range(0, len(disk_map), 2)):
        n_files = disk_map[j]
        n_free = 0

        if j + 1 < len(disk_map):
            n_free = disk_map[j + 1]

        blocks += n_files * [i] + n_free * ['.']
        files_map += [(i, offset, n_files)]
        free_map += [(offset + n_files, n_free)]
        offset += n_files + n_free

    return blocks, files_map, free_map

def compact_files(blocks, files_map, free_map):
    new_blocks = copy.deepcopy(blocks)

    for file in files_map[::-1]:
        idx, pos, n_files = file

        for k, free_space in enumerate(free_map):
            free_pos, n_free = free_space

            if n_free >= n_files:
                for i in range(n_files):
                    new_blocks[free_pos + i] = idx
                    new_blocks[pos + i] = '.'

                free_space = (free_pos + n_files, n_free - n_files)
                break

        if free_space[1] == 0:
            del free_map[k]
        else:
            free_map[k] = free_space

    return new_blocks

def checksum(blocks):
    return sum([i * b for i, b in enumerate(blocks) if b != '.'])

blocks, files_map, free_map = convert_to_blocks(disk_map)
# print(blocks)
blocks = compact_files(blocks, files_map, free_map)
# print(blocks)
print(checksum(blocks))