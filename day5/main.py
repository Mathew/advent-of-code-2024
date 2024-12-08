from collections import defaultdict

from input import ORDERINGS, PRINTINGS


def group_orderings(orderings):
    order = defaultdict(list)
    for before, after in orderings:
        order[before].append(after)

    return order

def is_printing_ordered(groups, printing):
    seen = []
    for p in reversed(printing):
        if p in seen:
            return False

        if p in groups.keys():
            seen.extend(groups[p])

    return True


def part_one(groups, printings) -> int:
    total = 0
    for prints in printings:
        if is_printing_ordered(groups, prints):
            total += prints[len(prints) // 2]

    return total


def main():
    groups = group_orderings(ORDERINGS)

    print(part_one(groups, PRINTINGS))

if __name__ == "__main__":
    main()
