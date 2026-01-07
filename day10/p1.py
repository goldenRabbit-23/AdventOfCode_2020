import sys


def main():
    data = open(sys.argv[1]).read().split('\n')
    jolts = sorted(int(x) for x in data)
    jolts = [0] + jolts + [jolts[-1] + 3]
    diffs = [jolts[i + 1] - jolts[i] for i in range(len(jolts) - 1)]
    print(diffs.count(1) * diffs.count(3))


if __name__ == '__main__':
    main()
