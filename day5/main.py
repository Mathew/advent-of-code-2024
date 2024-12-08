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

def order_printing(groups, printing):
    ordered_printing = []
    # track seen orderings to original number
    seen = defaultdict(list)

    for p in reversed(printing):
        if p in seen.keys():
            pos = max(ordered_printing.index(v) for v in seen[p])
            ordered_printing.insert(pos+1, p)
        else:
            ordered_printing.insert(0, p)

        if p in groups.keys():
            for v in groups[p]:
                seen[v].append(p)

    return ordered_printing

def part_two(groups, printings) -> int:
    total = 0
    for prints in printings:
        if not is_printing_ordered(groups, prints):
            fixed_p = order_printing(groups, prints)
            total += fixed_p[len(fixed_p) // 2]

    return total


def main():
    groups = group_orderings(ORDERINGS)

    print(part_one(groups, PRINTINGS))
    print(part_two(groups, PRINTINGS))

if __name__ == "__main__":
    main()
