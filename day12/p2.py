import sys


def main():
    data = open(sys.argv[1]).read().split('\n')
    instructions = [(line[0], int(line[1:])) for line in data]
    x, y, vx, vy = 0, 0, 10, 1  # ship (x,y), ship -> waypoint vector (vx,vy)

    for action, value in instructions:
        if action == 'N': vy += value
        elif action == 'S': vy -= value
        elif action == 'E': vx += value
        elif action == 'W': vx -= value
        elif action == 'L':
            for _ in range(value // 90): vx, vy = -vy, vx
        elif action == 'R':
            for _ in range(value // 90): vx, vy = vy, -vx
        elif action == 'F':
            x += vx * value
            y += vy * value

    print(abs(x) + abs(y))


if __name__ == '__main__':
    main()
