import sys


def main():
    data = open(sys.argv[1]).read().split('\n')
    print(max(int(line.translate(str.maketrans('FBLR', '0101')), 2) for line in data))


if __name__ == '__main__':
    main()
