import itertools


def get_lists() -> tuple[list[int], list[int]]:
    l1, l2 = [], []
    
    with open("input1.csv") as f:
        for line in f.readlines():
            line = line.replace("   ", ",")
            li1, li2 = line.split(",")
            l1.append(int(li1))
            l2.append(int(li2))

    return l1, l2


def part_one(list_one: list[int], list_two: list[int]) -> int:
    combined = zip(sorted(list_one), sorted(list_two))

    total_distance = 0
    for x, y in combined:
        total_distance += abs(y - x)

    return total_distance


def part_two(list_one, list_two) -> int:
    groups = itertools.groupby(sorted(list_two))
    counts = {}
    for x, y in groups:
        counts[x] = len(list(y)) 

    similarity = 0
    for x in list_one:
        similarity += x * counts.get(x, 0)

    return similarity


def main():
    list_one, list_two = get_lists()

    print(part_one(list_one, list_two))
    print(part_two(list_one, list_two))


if __name__ == "__main__":
    main()
