import numpy as np


input_txt = open("input.txt").read()
machines = input_txt.split("\n\n")
offset = 10000000000000

def get_machine_info(machine):
    machine_info = machine.split("\n")
    button_a = [int(x.split('+')[1]) for x in machine_info[0].split(": ")[1].split(", ")]
    button_b = [int(x.split('+')[1]) for x in machine_info[1].split(": ")[1].split(", ")]
    prize = [int(x.split('=')[1]) + offset for x in machine_info[2].split(": ")[1].split(", ")]

    return button_a, button_b, prize

def solve(a, b, p):
    A = np.asarray([[a[0], b[0]], [a[1], b[1]]]).astype(np.float64)
    B = np.asarray(p).astype(np.float64)
    s = np.linalg.solve(A, B)

    return s

def cost(a, b):
    return 3 * a + b

def is_valid(x, a, y, b, p):
    return a[0] * x + b[0] * y == p[0] and a[1] * x + b[1] * y == p[1]

total_cost = 0

for machine in machines:
    a, b, p = get_machine_info(machine)
    s = solve(a, b, p)

    a_times, b_times = np.round(s).astype(np.int64)
    valid = is_valid(a_times, a, b_times, b, p)

    if valid:
        total_cost += cost(a_times, b_times)

print(total_cost)