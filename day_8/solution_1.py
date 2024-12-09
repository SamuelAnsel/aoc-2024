input_text = open("input.txt").read()
input_text = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

OP = ['*', '+']

def is_solvable(result, numbers):
    if len(numbers) == 1:
        return result == numbers[0]
    
    solvable = False

    for op in OP:
        r = eval(f"numbers[0] {op} numbers[1]")

        if r <= result:
            solvable |= is_solvable(result, [r, *numbers[2:]])

    return solvable

calib_res = 0

for eq in input_text.splitlines():
    res, numbers = eq.split(':')
    res = int(res)
    
    numbers = [int(x) for x in numbers.strip().split(' ')]

    if is_solvable(res, numbers):
        calib_res += res

print(calib_res)