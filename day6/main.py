from dataclasses import dataclass


@dataclass
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __equals__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Guard:
    position: Position
    vector: Position
    walked: list[Position]

    UP = Position(0, -1)
    RIGHT = Position(1, 0)
    DOWN = Position(0,1)
    LEFT = Position(-1, 0)

    def __init__(self, position):
        self.position = position
        self.walked = [position, ]
        self.vector = self.UP

    def walk(self, grid):
        walking = True
        while(walking):
            walking = self._step_once(grid)

        return self._positions()

    def _step_once(self, grid) -> bool:
        lookahead = self.position + self.vector

        if lookahead.x == len(grid[0]) or lookahead.y == len(grid):
            return False

        if grid[lookahead.y][lookahead.x] == "#":
            self._turn()
            return True

        self.position = lookahead
        self.walked.append(self.position)
        return True

    def _turn(self):
        turns = [self.UP, self.RIGHT, self.DOWN, self.LEFT, ]
        indx = turns.index(self.vector)
        if indx == len(turns) - 1:
            indx = -1

        self.vector = turns[indx+1]

    def _positions(self):
        return set(self.walked)


def parse_grid(lines):
    grid = []
    for l in lines:
        grid.append([c for c in l if c != "\n"])

    return grid


def load_data() -> list[list[str]]:
    with open("input.csv") as f:
        return parse_grid(f.readlines())


def find_guard(grid: list[list[str]]) -> Guard:
    for y in range(len(grid)):
        if "^" in grid[y]:
            return Guard(Position(grid[y].index("^"), y))
    raise Exception("Guard Not Found")


def part_one():
    grid = load_data()
    guard = find_guard(grid)
    unq_pos = guard.walk(grid)
    print(len(unq_pos))


def main():
    part_one()

if __name__ == "__main__":
    main()

