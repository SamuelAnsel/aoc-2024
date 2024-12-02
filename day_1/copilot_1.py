def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

def parse_input(input_str):
    left_list = []
    right_list = []
    for line in input_str.strip().split('\n'):
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    return left_list, right_list

# Example usage
input_str = open("input.txt").read()
left_list, right_list = parse_input(input_str)
total_distance = calculate_total_distance(left_list, right_list)
print(f"Total distance: {total_distance}")
