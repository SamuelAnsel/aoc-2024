input_text = open("input.txt").read()

reports = input_text.strip().split('\n')
safe_count = 0

for report in reports:
    levels = [int(level) for level in report.split(' ')]

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

    if safe:
        safe_count += 1

print(safe_count)