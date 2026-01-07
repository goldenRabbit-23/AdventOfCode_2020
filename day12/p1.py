import sys


def main():
    data = open(sys.argv[1]).read().split('\n')
    instructions = [(line[0], int(line[1:])) for line in data]
    x, y = 0, 0
    direction = 0  # 0: east, 1: south, 2: west, 3: north

    dmoves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for action, value in instructions:
        if action == 'N': y += value
        elif action == 'S': y -= value
        elif action == 'E': x += value
        elif action == 'W': x -= value
        elif action == 'L': direction = (direction - value // 90) % 4
        elif action == 'R': direction = (direction + value // 90) % 4
        elif action == 'F':
            dx, dy = dmoves[direction]
            x, y = x + dx * value, y + dy * value

    print(abs(x) + abs(y))


if __name__ == '__main__':
    main()
