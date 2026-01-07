import sys
from functools import cache


def main():
    data = open(sys.argv[1]).read().split('\n')
    jolts = sorted(int(x) for x in data)
    jolts = [0] + jolts + [jolts[-1] + 3]

    @cache
    def dfs(jolt):
        if jolt == jolts[-1]:
            return 1
        ways = 0
        for diff in (1, 2, 3):
            if jolt in jolts:
                ways += dfs(jolt + diff)
        return ways

    print(dfs(0))


if __name__ == '__main__':
    main()
