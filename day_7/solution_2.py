input_text = open("input.txt").read()

OP = ['*', '+', 'concat']

def is_solvable(result, numbers):
    if len(numbers) == 1:
        return result == numbers[0]
    
    solvable = False

    for op in OP:
        if op == 'concat':
            r = int(str(numbers[0]) + str(numbers[1]))
        else:
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