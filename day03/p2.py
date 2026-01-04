import sys


def main():
    data = open(sys.argv[1]).read().split('\n')
    grid = [list(line) for line in data]
    R, C = len(grid), len(grid[0])

    def count_trees(dr, dc):
        r, c = 0, 0
        trees = 0
        while r < R:
            trees += grid[r][c % C] == '#'
            r += dr
            c += dc
        return trees

    print(
        count_trees(1, 1) *
        count_trees(1, 3) *
        count_trees(1, 5) *
        count_trees(1, 7) *
        count_trees(2, 1)
    )


if __name__ == '__main__':
    main()
