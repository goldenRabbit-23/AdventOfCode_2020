import sys
from itertools import combinations


def main():
    data = open(sys.argv[1]).read().split('\n')
    numbers = [int(line) for line in data]
    p, q = next((a, b) for a, b in combinations(numbers, 2) if a + b == 2020)
    print(p * q)


if __name__ == '__main__':
    main()
