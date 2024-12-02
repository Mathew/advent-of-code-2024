def load_reports():
    reports = []

    with open("input.csv") as f:
        for line in f.readlines():
            levels = []

            for level in line.split(" "):
                levels.append(int(level))

            reports.append(levels)

    return reports


def is_report_safe(levels: list[int]) -> bool:
    incr = True
    x, y = levels[0], levels[1]

    if x > y:
        incr = False

    for l in range(0, len(levels)-1):
        n = levels[l] - levels[l+1]

        if abs(n) < 1 or abs(n) > 3:
            return False

        if n < 0 and incr is False:
            return False

        if n > 0 and incr is True:
            return False

        if n == 0:
            return False

    return True


def main():
    reports = load_reports()

    safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            safe_reports +=1

    print(safe_reports)


if __name__ == "__main__":
    main()
