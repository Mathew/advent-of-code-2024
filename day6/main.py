from copy import deepcopy
from dataclasses import dataclass


class InLoop(Exception):
    pass


@dataclass
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return abs((self.x - other.x) + (self.y - other.y))

    def __equals__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Guard:
    position: Position
    vector: Position
    walked: list[Position]
    turn_positions: list[tuple[Position, Position]]

    UP = Position(0, -1)
    RIGHT = Position(1, 0)
    DOWN = Position(0,1)
    LEFT = Position(-1, 0)

    def __init__(self, position):
        self.position = position
        self.walked = [position, ]
        self.vector = self.UP
        self.turn_positions = []

    def walk(self, grid, detect_loop=False):
        walking = True
        while(walking):
            walking = self._step_once(grid, detect_loop)

        return self._positions()

    def _step_once(self, grid, detect_loop=False) -> bool:
        lookahead = self.position + self.vector

        if lookahead.x == len(grid[0]) or lookahead.y == len(grid) or lookahead.x < 0 or lookahead.y < 0:
            return False

        if grid[lookahead.y][lookahead.x] == "#":
            if detect_loop:
                tup = (self.position, self.vector)

                if tup in self.turn_positions:
                    raise InLoop()

                self.turn_positions.append(tup)

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


def calculate_inf_loops(grid, guard):
    inf_loops = 0
    for pop in set(guard.walked[1:]):
        pop_grid = deepcopy(grid)
        guard = find_guard(pop_grid)
        pop_grid[pop.y][pop.x] = "#"

        if pop.y == guard.position.y and pop.x == guard.position.x:
            continue

        try:
            guard.walk(pop_grid, True)
        except InLoop:
            inf_loops += 1

    return inf_loops


def part_one():
    grid = load_data()
    guard = find_guard(grid)
    unq_pos = guard.walk(grid)


def part_two():
    grid = load_data()
    guard = find_guard(grid)
    guard.walk(grid)


def main():
    part_one()
    part_two()

if __name__ == "__main__":
    main()

