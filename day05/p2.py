import sys


def main():
    data = open(sys.argv[1]).read().split('\n')
    seats = [int(line.translate(str.maketrans('FBLR', '0101')), 2) for line in data]
    seats.sort()

    for s0, s1 in zip(seats, seats[1:]):
        if abs(s0 - s1) == 2:
            print((s0 + s1) // 2)
            break


if __name__ == '__main__':
    main()
