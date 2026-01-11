import sys
from itertools import product


def main():
    grid = open(sys.argv[1]).read().split('\n')
    active = {(r, c, 0) for r, row in enumerate(grid) for c, val in enumerate(row) if val == '#'}

    for _ in range(6):
        new_active = set()
        candidates = set()
        for x, y, z in active:
            for dx, dy, dz in product((-1, 0, 1), repeat=3):
                candidates.add((x + dx, y + dy, z + dz))

        for x, y, z in candidates:
            count = sum((x + dx, y + dy, z + dz) in active
                        for dx, dy, dz in product((-1, 0, 1), repeat=3)
                        if (dx, dy, dz) != (0, 0, 0))
            if (x, y, z) in active and count in (2, 3):
                new_active.add((x, y, z))
            elif (x, y, z) not in active and count == 3:
                new_active.add((x, y, z))
        active = new_active

    print(len(active))


if __name__ == '__main__':
    main()