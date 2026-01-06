import sys


def main():
    data = open(sys.argv[1]).read().split('\n\n')
    print(sum(len({answer for person in group.split('\n') for answer in person}) for group in data))


if __name__ == '__main__':
    main()
