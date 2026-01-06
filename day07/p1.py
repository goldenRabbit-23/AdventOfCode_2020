import sys
from collections import defaultdict


def main():
    data = open(sys.argv[1]).read().split('\n')
    parents_of = defaultdict(set)

    for line in data:
        parent, rhs = line.split(' bags contain ')
        if rhs.startswith('no'):
            continue
        for part in rhs[:-1].split(', '):
            w = part.split()
            color = f'{w[1]} {w[2]}'
            parents_of[color].add(parent)

    seen, stack = set(), ['shiny gold']

    while stack:
        c = stack.pop()
        for p in parents_of[c]:
            if p not in seen:
                seen.add(p)
                stack.append(p)

    print(len(seen))


if __name__ == '__main__':
    main()
