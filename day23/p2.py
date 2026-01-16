import sys


MAX_CUP = 1_000_000
MOVES = 10_000_000

def main():
    data = open(sys.argv[1]).read()
    cups = [int(x) for x in list(data)]

    next_cup = [i + 1 for i in range(MAX_CUP + 1)]
    next_cup[MAX_CUP] = cups[0]
    for c1, c2 in zip(cups, cups[1:]):
        next_cup[c1] = c2
    next_cup[cups[-1]] = max(cups) + 1

    current_cup = cups[0]
    for _ in range(MOVES):
        pick_up1 = next_cup[current_cup]
        pick_up2 = next_cup[pick_up1]
        pick_up3 = next_cup[pick_up2]

        destination_cup = current_cup - 1 or MAX_CUP
        while destination_cup in (pick_up1, pick_up2, pick_up3):
            destination_cup = destination_cup - 1 or MAX_CUP

        next_cup[current_cup] = next_cup[pick_up3]
        next_cup[pick_up3] = next_cup[destination_cup]
        next_cup[destination_cup] = pick_up1

        current_cup = next_cup[current_cup]

    print(next_cup[1] * next_cup[next_cup[1]])


if __name__ == '__main__':
    main()
