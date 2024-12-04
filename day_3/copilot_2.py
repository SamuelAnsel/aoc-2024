import re

def parse_instructions(memory):
    # Regular expression to find mul(X,Y) instructions
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    # Regular expression to find do() and don't() instructions
    control_pattern = re.compile(r"(do\(\)|don't\(\))")
    
    # Split the memory string into parts based on control instructions
    parts = control_pattern.split(memory)
    
    enabled = True
    total = 0
    
    for part in parts:
        if part == "do()":
            enabled = True
        elif part == "don't()":
            enabled = False
        else:
            if enabled:
                for match in mul_pattern.finditer(part):
                    x, y = map(int, match.groups())
                    total += x * y
    
    return total

# Example usage
memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
print(parse_instructions(memory))  # Output should be 161

memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print(parse_instructions(memory))  # Output should be 48

memory = open("input.txt").read()
print(parse_instructions(memory))  # Output should be 48