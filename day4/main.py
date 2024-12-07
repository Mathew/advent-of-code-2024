from copy import deepcopy
from dataclasses import dataclass

ORDERED_LETTERS = ["X", "M", "A", "S"]


@dataclass
class Position:
    x: int
    y: int

class Path:
    vector: Position
    position: Position

    def __init__(self, pos_x, pos_y, vx, vy):
        self.vector = Position(vx, vy)
        self.position = Position(pos_x, pos_y)

    def next_position(self, max_x, max_y) -> "Path":
        p = Path(
            self.vector.x + self.position.x, self.vector.y + self.position.y, 
            self.vector.x, self.vector.y
        )

        if (
            p.position.x < 0 or p.position.y < 0 or 
            p.position.x > max_x or p.position.y > max_y
        ):
            raise IndexError()

        return p

def calculate_radial_search_path(x:int, y: int, max_x: int, max_y:int) -> list[Path]:
    vectors = [(-1, -1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, 1), (0, -1), (1, -1)]
    path = []
    for vx, vy in vectors:
        if x + vx > -1 and y + vy > -1 and x + vx < max_x and y + vy < max_y:
            path.append(Path(x + vx, y + vy, vx, vy))

    return path


def load_data():

    data = []
    with open("input.csv") as f:
        for line in f.readlines():
            data.append([c for c in line if c != "\n"])

    return data


def letters_to_positions(data):
    starting_positions = []

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "X":
                starting_positions.append((x, y))

    return starting_positions

def search_from_position(position, data) -> int:
    xstart, ystart = position 
    path = calculate_radial_search_path(xstart, ystart, len(data[0]), len(data[1]))

    count = 0
    valid_path_contents = ["M", "A", "S"]
    position = path[0]

    for angle in path:

        position = angle
        index = 0
        good_path = True
        while(good_path):
            if data[position.position.y][position.position.x] == valid_path_contents[index]:
                try:
                    position = position.next_position(len(data) - 1, len(data[0]) - 1)
                except IndexError:
                    good_path = False

                if index == len(valid_path_contents) - 1:
                    count += 1
                    good_path = False

                index += 1

            else:
                good_path = False


    return count

def count_xmas(data) -> int:
    starting_positions = letters_to_positions(data)

    count = 0
    for xstart, ystart in starting_positions:
        num_found = search_from_position((xstart, ystart), data)
        count += num_found

    return count

def part_one(data: list[list[str]]):
    print(count_xmas(data))


def main():
    data = load_data()
    part_one(data)


if __name__ == "__main__":
    main()
