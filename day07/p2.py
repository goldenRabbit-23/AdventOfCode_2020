import sys
from collections import defaultdict


def main():
    data = open(sys.argv[1]).read().split('\n')
    children_of = defaultdict(set)

    for line in data:
        parent, rhs = line.split(' bags contain ')
        if rhs.startswith('no'):
            continue
        for part in rhs[:-1].split(', '):
            w = part.split()
            color = f'{w[1]} {w[2]}'
            children_of[parent].add((color, int(w[0])))

    def dfs(color):
        return sum(n * (1 + dfs(child)) for child, n in children_of[color])

    print(dfs('shiny gold'))


if __name__ == '__main__':
    main()
