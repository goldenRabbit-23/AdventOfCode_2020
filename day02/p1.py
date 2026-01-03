import sys
import re


def main():
    data = open(sys.argv[1]).read().split('\n')
    valid = 0

    for line in data:
        m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
        if m:
            min_count, max_count = int(m.group(1)), int(m.group(2))
            letter, password = m.group(3), m.group(4)
        if min_count <= password.count(letter) <= max_count:
            valid += 1

    print(valid)


if __name__ == '__main__':
    main()
