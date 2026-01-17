import sys


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

    print(len(black))


if __name__ == '__main__':
    main()
