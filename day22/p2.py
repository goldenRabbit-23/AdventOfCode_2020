import sys


def main():
    p1, p2 = open(sys.argv[1]).read().split('\n\n')
    p1 = [int(x) for x in p1.split('\n')[1:]]
    p2 = [int(x) for x in p2.split('\n')[1:]]

    def play(p1, p2):
        seen = set()

        while p1 and p2:
            state = (tuple(p1), tuple(p2))
            if state in seen:
                return 1, p1
            seen.add(state)

            c1 = p1.pop(0)
            c2 = p2.pop(0)

            if c1 <= len(p1) and c2 <= len(p2):
                winner, _ = play(p1[:c1], p2[:c2])
            else:
                winner = 1 if c1 > c2 else 2

            if winner == 1:
                p1 += [c1, c2]
            else:
                p2 += [c2, c1]

        return (1, p1) if p1 else (2, p2)

    _, winner_deck = play(p1, p2)
    print(sum(i * v for i, v in enumerate(reversed(winner_deck), 1)))


if __name__ == '__main__':
    main()
