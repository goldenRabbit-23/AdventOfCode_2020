import sys
from itertools import product


def main():
    grid = open(sys.argv[1]).read().split('\n')
    active = {(r, c, 0, 0) for r, row in enumerate(grid) for c, val in enumerate(row) if val == '#'}

    for _ in range(6):
        new_active = set()
        candidates = set()
        for x, y, z, w in active:
            for dx, dy, dz, dw in product((-1, 0, 1), repeat=4):
                candidates.add((x + dx, y + dy, z + dz, w + dw))

        for x, y, z, w in candidates:
            count = sum((x + dx, y + dy, z + dz, w + dw) in active
                        for dx, dy, dz, dw in product((-1, 0, 1), repeat=4)
                        if (dx, dy, dz, dw) != (0, 0, 0, 0))
            if (x, y, z, w) in active and count in (2, 3):
                new_active.add((x, y, z, w))
            elif (x, y, z, w) not in active and count == 3:
                new_active.add((x, y, z, w))
        active = new_active

    print(len(active))


if __name__ == '__main__':
    main()