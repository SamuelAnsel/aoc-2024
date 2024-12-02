def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def can_be_safe_by_removing_one(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report) or can_be_safe_by_removing_one(report):
            safe_count += 1
    return safe_count

# Example data
data = open("input.txt").read()

# Parse the data
reports = [list(map(int, line.split())) for line in data.strip().split('\n')]

# Count safe reports
safe_reports = count_safe_reports(reports)
print(safe_reports)
