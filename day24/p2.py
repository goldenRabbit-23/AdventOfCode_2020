import sys
from collections import Counter


DIR = {
    'e': (1, 0),
    'w': (-1, 0),
    'se': (1, -1),
    'nw': (-1, 1),
    'sw': (0, -1),
    'ne': (0, 1),
}

def main():
    data = open(sys.argv[1]).read().split('\n')
    black = set()

    for line in data:
        u, v = 0, 0
        i = 0
        while i < len(line):
            if line[i] in 'ns':
                d = line[i:i+2]
                i += 2
            else:
                d = line[i]
                i += 1

            du, dv = DIR[d]
            u, v = u + du, v + dv

        if (u, v) in black:
            black.remove((u, v))
        else:
            black.add((u, v))

    for _ in range(100):
        c = Counter()

        for u, v in black:
            for du, dv in DIR.values():
                c[(u + du, v + dv)] += 1

        new_black = set()

        for pos, cnt in c.items():
            if pos in black:
                if cnt in (1, 2):
                    new_black.add(pos)
            else:
                if cnt == 2:
                    new_black.add(pos)

        black = new_black

    print(len(black))


if __name__ == '__main__':
    main()
