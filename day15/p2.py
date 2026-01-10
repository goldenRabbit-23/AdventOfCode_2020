import sys


def main():
    data = open(sys.argv[1]).read()
    numbers = [int(x) for x in data.split(',')]
    last_spoken = [0] * 30000000
    last_number = numbers[-1]
    turn = len(numbers) + 1

    for idx, num in enumerate(numbers[:-1], 1):
        last_spoken[num] = idx

    while turn <= 30000000:
        prev_turn = last_spoken[last_number]
        if prev_turn != 0:
            next_number = turn - 1 - prev_turn
        else:
            next_number = 0
        last_spoken[last_number] = turn - 1
        last_number = next_number
        turn += 1

    print(last_number)


if __name__ == '__main__':
    main()
