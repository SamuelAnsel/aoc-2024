import numpy as np


input_text = open("input.txt", "r").read()
input_text = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

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

def move(warehouse_map, instruction, object_pos=None):
    if object_pos is None:
        pos = np.where(warehouse_map == "@")
        i, j = pos[0][0], pos[1][0]
        object_char = "@"
    else:
        i, j = object_pos
        object_char = warehouse_map[i, j]

    direction = directions[instruction]
    new_position = (i + direction[0], j + direction[1])
    has_moved = False
    
    if warehouse_map[new_position] == ".":
        warehouse_map[i, j] = "."
        warehouse_map[new_position] = object_char
        has_moved = True
    
    elif warehouse_map[new_position] in ['[', ']']:
        if instruction in ['<', '>']:
            warehouse_map, has_moved = move(warehouse_map, instruction, new_position)
        else:
            

        if has_moved:
            warehouse_map[i, j] = "."
            warehouse_map[new_position] = object_char
    
    return warehouse_map, has_moved

def boxes_score(warehouse_map):
    boxes_positions = np.where(warehouse_map == "O")
    boxes_score = 0

    for i, j in zip(boxes_positions[0], boxes_positions[1]):
        boxes_score += 100 * i + j

    return boxes_score

print(warehouse_map)

# for instruction in instructions:
#     warehouse_map, has_moved = move(warehouse_map, instruction)

print(boxes_score(warehouse_map))