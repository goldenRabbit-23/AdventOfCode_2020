import sys
from math import prod


def main():
    fields, my, nearby = open(sys.argv[1]).read().split('\n\n')
    my = [int(x) for x in my.split('\n')[1].split(',')]

    rules = {}
    for line in fields.split('\n'):
        name, ranges = line.split(': ')
        rules[name] = [tuple(map(int, r.split('-'))) for r in ranges.split(' or ')]

    def is_valid(num):
        return any(s <= num <= e for rngs in rules.values() for s, e in rngs)

    valid_tickets = []
    for line in nearby.split('\n')[1:]:
        t = [int(x) for x in line.split(',')]
        if all(is_valid(n) for n in t):
            valid_tickets.append(t)

    candidates = {
        name: {
            i for i in range(len(my))
            if all(any(s <= ticket[i] <= e for s, e in rngs) for ticket in valid_tickets)
        }
        for name, rngs in rules.items()
    }

    final_map = {}
    while candidates:
        name, possible = min(candidates.items(), key=lambda x: len(x[1]))
        col = possible.pop()
        final_map[name] = col
        del candidates[name]
        for opts in candidates.values():
            opts.discard(col)

    print(prod(my[col] for name, col in final_map.items() if name.startswith('departure')))


if __name__ == '__main__':
    main()
