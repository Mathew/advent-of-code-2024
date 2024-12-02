def load_reports():
    reports = []

    with open("input.csv") as f:
        for line in f.readlines():
            levels = []

            for level in line.split(" "):
                levels.append(int(level))

            reports.append(levels)

    return reports


def is_report_safe(levels: list[int], dampen=False):
    if sorted(levels) != levels and sorted(levels, reverse=True) != levels:
        return False

    results = [abs(levels[i] - levels[i+1]) for i in range(len(levels) - 1)]
    filtered = [r for r in results if r > 0 and r < 4]

    return len(list(filtered)) == len(results)


def is_report_safe_dampened(levels: list[int]):
    if is_report_safe(levels):
        return True

    for index in range(0, len(levels)):
        cl = levels.copy()
        cl.pop(index)
        if is_report_safe(cl):
            return True

    return False


def main():
    reports = load_reports()

    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports +=1
    print(safe_reports)

    safe_reports = 0
    for report in reports:
        if is_report_safe_dampened(report):
            safe_reports +=1
    print(safe_reports)


if __name__ == "__main__":
    main()
