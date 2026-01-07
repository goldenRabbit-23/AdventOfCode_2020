import sys


DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def main():
    data = open(sys.argv[1]).read().split('\n')
    grid = [list(row) for row in data]
    R, C = len(grid), len(grid[0])

    def visible_occupied(r, c):
        occupied = 0
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            while 0 <= nr < R and 0 <= nc < C:
                if grid[nr][nc] == 'L':
                    break
                if grid[nr][nc] == '#':
                    occupied += 1
                    break
                nr += dr
                nc += dc
        return occupied

    while True:
        new_grid = [row[:] for row in grid]
        changed = False

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.':
                    continue

                occupied = visible_occupied(r, c)

                if grid[r][c] == 'L' and occupied == 0:
                    new_grid[r][c] = '#'
                    changed = True
                elif grid[r][c] == '#' and occupied >= 5:
                    new_grid[r][c] = 'L'
                    changed = True

        if not changed:
            break

        grid = new_grid

    print(sum(row.count('#') for row in grid))


if __name__ == '__main__':
    main()
