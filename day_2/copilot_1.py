def is_safe_report(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def count_safe_reports(data):
    reports = [list(map(int, line.split())) for line in data.strip().split('\n')]
    return sum(1 for report in reports if is_safe_report(report))

if __name__ == "__main__":
    data = open("input.txt").read()
    print(count_safe_reports(data))
