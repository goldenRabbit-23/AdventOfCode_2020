import sys


def main():
    fields, _, nearby = open(sys.argv[1]).read().split('\n\n')
    ranges = []

    for line in fields.split('\n'):
        parts = line.split(': ')[1].split(' or ')
        for part in parts:
            start, end = map(int, part.split('-'))
            ranges.append((start, end))

    error_rate = 0

    for line in nearby.split('\n')[1:]:
        numbers = map(int, line.split(','))
        for number in numbers:
            if not any(start <= number <= end for start, end in ranges):
                error_rate += number

    print(error_rate)


if __name__ == '__main__':
    main()
