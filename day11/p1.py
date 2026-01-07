import sys


DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def main():
    data = open(sys.argv[1]).read().split('\n')
    grid = [list(row) for row in data]
    R, C = len(grid), len(grid[0])

    while True:
        new_grid = [row[:] for row in grid]
        changed = False

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.':
                    continue

                occupied = sum(
                    0 <= r + dr < R and 0 <= c + dc < C and grid[r + dr][c + dc] == '#'
                    for dr, dc in DIRS
                )

                if grid[r][c] == 'L' and occupied == 0:
                    new_grid[r][c] = '#'
                    changed = True
                elif grid[r][c] == '#' and occupied >= 4:
                    new_grid[r][c] = 'L'
                    changed = True

        if not changed:
            break

        grid = new_grid

    print(sum(row.count('#') for row in grid))


if __name__ == '__main__':
    main()
