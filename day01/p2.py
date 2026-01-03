import sys
from itertools import combinations


def main():
    data = open(sys.argv[1]).read().split('\n')
    numbers = [int(line) for line in data]
    p, q, r = next((a, b, c) for a, b, c in combinations(numbers, 3) if a + b + c == 2020)
    print(p * q * r)


if __name__ == '__main__':
    main()
