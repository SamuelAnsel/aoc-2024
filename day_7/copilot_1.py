from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

def is_valid_equation(target, numbers):
    for operators in product('+-*', repeat=len(numbers) - 1):
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def total_calibration_result(input_str):
    total = 0
    for line in input_str.strip().split('\n'):
        target, numbers = line.split(': ')
        target = int(target)
        numbers = list(map(int, numbers.split()))
        if is_valid_equation(target, numbers):
            total += target
    return total

# Example usage
input_str = open("input.txt").read()

print(total_calibration_result(input_str))
