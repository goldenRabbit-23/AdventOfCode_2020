import sys


def main():
    p1, p2 = open(sys.argv[1]).read().split('\n\n')
    p1 = [int(x) for x in p1.split('\n')[1:]]
    p2 = [int(x) for x in p2.split('\n')[1:]]

    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]

    winner = p1 if p1 else p2
    print(sum(i * v for i, v in enumerate(reversed(winner), 1)))


if __name__ == '__main__':
    main()
