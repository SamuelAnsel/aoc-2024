import numpy as np
from collections import deque


input_text = open("input.txt", "r").read()

warehouse_map = np.asarray([list(row) for row in input_text.split("\n\n")[0].split("\n")])
new_warehouse_map = np.zeros((warehouse_map.shape[0], warehouse_map.shape[1] * 2), dtype=str)

for i in range(warehouse_map.shape[0]):
    for j in range(warehouse_map.shape[1]):
        if warehouse_map[i, j] == "@":
            new_warehouse_map[i, 2 * j ] = warehouse_map[i, j]
            new_warehouse_map[i, 2 * j  + 1] = '.'        
        elif warehouse_map[i, j] == "#":
            new_warehouse_map[i, 2 * j] = warehouse_map[i, j]
            new_warehouse_map[i, 2 * j + 1] = '#'
        elif warehouse_map[i, j] == ".":            
            new_warehouse_map[i, 2 * j ] = warehouse_map[i, j]
            new_warehouse_map[i, 2 * j  + 1] = '.'
        elif warehouse_map[i, j] == "O":
            new_warehouse_map[i, 2 * j ] = '['
            new_warehouse_map[i, 2 * j  + 1] = ']'

warehouse_map = new_warehouse_map

instructions = input_text.split("\n\n")[1].replace('\n', '')
directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

def position_key(pos):
    return str(pos[0]) + "," + str(pos[1])

def get_boxes_ref(warehouse_map):
    boxes = dict()
    positions = dict()

    left_positions = np.asarray(np.where(warehouse_map == "[")).reshape(2, -1).T

    for i, left_pos in enumerate(left_positions):
        boxes[i] = np.asarray([left_pos, [left_pos[0], left_pos[1] + 1]])
        positions[position_key(boxes[i][0])] = i
        positions[position_key(boxes[i][1])] = i

    return boxes, positions

def get_impacted_boxes(push_pos, boxes, positions, instruction):
    impacted_boxes = []
    queue = deque([positions.get(position_key(push_pos))])
    dir = np.asarray(directions[instruction])

    while len(queue) != 0:
        box_idx = queue.popleft()
        impacted_boxes += [box_idx]

        left_pos, right_pos = boxes[box_idx][0], boxes[box_idx][1]

        if instruction in ['v', '^']:
            left_key, right_key = position_key(left_pos + dir), position_key(right_pos + dir)
            add_boxes = list()

            if left_key in positions:
                add_boxes += [positions[left_key]]

            if right_key in positions:
                add_boxes += [positions[right_key]]

            add_boxes = list(set(add_boxes))

            for x in add_boxes:
                queue.append(x)
        elif instruction == "<":
            key = position_key(left_pos + dir)

            if key in positions:
                queue.append(positions[key])
        else:
            key = position_key(right_pos + dir)

            if key in positions:
                queue.append(positions[key])

    return impacted_boxes
        
def can_move(warehouse_map, box_idx, boxes, instruction):
    dir = np.asarray(directions[instruction])

    for idx in box_idx:
        left_pos, right_pos = boxes[idx][0], boxes[idx][1]

        for pos in [left_pos, right_pos]:
            p = pos + dir
            if warehouse_map[p[0], p[1]] == "#":
                return False
            
    return True

def move_boxes(warehouse_map, box_idx, boxes, instruction):
    dir = np.asarray(directions[instruction])
    box_idx = sorted(box_idx)

    if instruction in ["v", ">"]:
        box_idx = box_idx[::-1]
    
    for idx in box_idx:
        left_pos, right_pos = boxes[idx][0], boxes[idx][1]
        warehouse_map[left_pos[0], left_pos[1]] = "."
        warehouse_map[right_pos[0], right_pos[1]] = "."
        left_pos, right_pos = boxes[idx][0] + dir, boxes[idx][1] + dir
        warehouse_map[left_pos[0], left_pos[1]] = "["
        warehouse_map[right_pos[0], right_pos[1]] = "]"

def move(warehouse_map, instruction):
    pos = np.where(warehouse_map == "@")
    i, j = pos[0][0], pos[1][0]

    direction = directions[instruction]
    new_position = (i + direction[0], j + direction[1])
    
    if warehouse_map[new_position] == ".":
        warehouse_map[i, j] = "."
        warehouse_map[new_position] = "@"

    elif warehouse_map[new_position] in ['[', ']']:
        boxes, positions = get_boxes_ref(warehouse_map)
        box_idx = get_impacted_boxes(new_position, boxes, positions, instruction)

        if can_move(warehouse_map, box_idx, boxes, instruction):
            move_boxes(warehouse_map, box_idx, boxes, instruction)
            warehouse_map[i, j] = "."
            warehouse_map[new_position] = "@"  
    
    return warehouse_map

def boxes_score(warehouse_map):
    boxes_score = 0

    boxes_positions = np.where(warehouse_map == "[")

    for i, j in zip(boxes_positions[0], boxes_positions[1]):
        boxes_score += 100 * i + j

    return boxes_score


for instruction in instructions:
    warehouse_map = move(warehouse_map, instruction)

print(boxes_score(warehouse_map))