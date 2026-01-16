import sys


def main():
    data = open(sys.argv[1]).read()
    cups = [int(x) for x in list(data)]

    for _ in range(100):
        current_cup = cups[0]
        pick_up = cups[1:4]
        cups = [cups[0]] + cups[4:]

        destination_cup = current_cup - 1 or 9
        while destination_cup in pick_up:
            destination_cup = destination_cup - 1 or 9

        dest_idx = cups.index(destination_cup) + 1
        cups = cups[:dest_idx] + pick_up + cups[dest_idx:]
        cups = cups[1:] + [cups[0]]

    one_idx = cups.index(1)
    print(''.join(str(cup) for cup in cups[one_idx + 1:] + cups[:one_idx]))


if __name__ == '__main__':
    main()
