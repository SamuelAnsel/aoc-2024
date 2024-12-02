input_text = open("input.txt").read()

reports = input_text.strip().split('\n')
safe_count = 0

def report_is_safe(levels):
    safe = True
    prev_direction = 0

    for i in range(len(levels) - 1):
        if not(1 <= abs(levels[i] - levels[i + 1]) <= 3):
            safe = False
            break

        direction = levels[i + 1] - levels[i]

        if prev_direction * direction < 0:
            safe = False
            break

        prev_direction = direction

    return safe

for report in reports:
    levels = [int(level) for level in report.split(' ')]

    safe = False
    for i in range(len(levels)):
        new_levels = levels.copy()
        new_levels.pop(i)

        if report_is_safe(new_levels):
            safe_count += 1
            break

print(safe_count)