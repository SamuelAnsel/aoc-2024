from itertools import product

def parse_input(input_str):
    equations = []
    for line in input_str.strip().split('\n'):
        target, numbers = line.split(': ')
        target = int(target)
        numbers = list(map(int, numbers.split()))
        equations.append((target, numbers))
    return equations

def evaluate_expression(numbers, operators):
    expression = str(numbers[0])
    for i in range(1, len(numbers)):
        expression += operators[i-1] + str(numbers[i])
    return eval(expression.replace('||', ''))

def generate_operator_combinations(length):
    return product(['+', '*', '||'], repeat=length-1)

def is_valid_equation(target, numbers):
    for operators in generate_operator_combinations(len(numbers)):
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def calculate_total_calibration_result(input_str):
    equations = parse_input(input_str)
    total = 0
    for target, numbers in equations:
        if is_valid_equation(target, numbers):
            total += target
    return total

# Example usage
input_str = open("input.txt").read()

print(calculate_total_calibration_result(input_str))
