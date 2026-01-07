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
            break

    for i in range(len(numbers)):
        for l in range(2, len(numbers) - i):
            contiguous_range = numbers[i:i + l]
            if sum(contiguous_range) > target:
                break
            if sum(contiguous_range) == target:
                print(min(contiguous_range) + max(contiguous_range))
                return


if __name__ == '__main__':
    main()
