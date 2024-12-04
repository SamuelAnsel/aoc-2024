import re

def sum_valid_multiplications(corrupted_memory):
    # Regular expression to find valid mul(X,Y) instructions
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    matches = pattern.findall(corrupted_memory)
    
    total_sum = 0
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y
    
    return total_sum

# Example usage
corrupted_memory = open("input.txt").read()
print(sum_valid_multiplications(corrupted_memory))  # Output should be 161
