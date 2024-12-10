def compact_disk_map(disk_map):
    # Parse the disk map into blocks
    blocks = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1])
        blocks.append((file_length, free_length))

    # Create the initial block representation
    block_representation = []
    file_id = 0
    for file_length, free_length in blocks:
        block_representation.extend([str(file_id)] * file_length)
        block_representation.extend(['.'] * free_length)
        file_id += 1

    # Compact the blocks
    compacted_blocks = []
    for block in block_representation:
        if block != '.':
            compacted_blocks.append(block)
    compacted_blocks.extend(['.'] * (len(block_representation) - len(compacted_blocks)))

    # Calculate the checksum
    checksum = 0
    for position, block in enumerate(compacted_blocks):
        if block != '.':
            checksum += position * int(block)

    return checksum

# Example usage
input = open("input.txt").read().strip()
print(compact_disk_map(input))
