import sys


def main():
    data = open(sys.argv[1]).read().split('\n\n')
    print(sum(len(set.intersection(*(set(person) for person in group.split('\n')))) for group in data))


if __name__ == '__main__':
    main()
