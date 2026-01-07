import sys
from itertools import combinations


def main():
    data = open(sys.argv[1]).read().split('\n')
    numbers = [int(x) for x in data]
    preamble_length = 25

    for i in range(preamble_length, len(numbers)):
        preamble = numbers[i - preamble_length:i]
        target = numbers[i]
        if not any(a + b == target for a, b in combinations(preamble, 2)):
            print(target)
            break


if __name__ == '__main__':
    main()
