import csv




def get_lists() -> tuple[list[int], list[int]]:
    l1, l2 = [], []
    
    with open("input1.csv") as f:
        for line in f.readlines():
            line = line.replace("   ", ",")
            li1, li2 = line.split(",")
            l1.append(int(li1))
            l2.append(int(li2))

    return l1, l2


def main():
    list_one, list_two = get_lists()
    combined = zip(sorted(list_one), sorted(list_two))

    total_distance = 0
    for x, y in combined:
        total_distance += abs(y - x)

    print(total_distance)



if __name__ == "__main__":
    main()
