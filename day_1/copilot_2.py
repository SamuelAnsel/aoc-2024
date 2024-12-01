def calculate_similarity_score(input_str):
    lines = input_str.strip().split('\n')
    left_list = []
    right_list = []
    
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_list.count(num)
    
    return similarity_score

# Example usage
input_data = open("input.txt").read()
print(calculate_similarity_score(input_data))  # Output should be 31
