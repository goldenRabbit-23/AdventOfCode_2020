import sys


SUBJECT_NUMBER = 7
DIVISOR = 20201227

def main():
    data = open(sys.argv[1]).read().split('\n')
    card_pubkey = int(data[0])
    door_pubkey = int(data[1])

    card_loop_size = 0
    value = 1

    while value != card_pubkey:
        value = (value * SUBJECT_NUMBER) % DIVISOR
        card_loop_size += 1

    encryption_key = 1
    for _ in range(card_loop_size):
        encryption_key = (encryption_key * door_pubkey) % DIVISOR

    print(encryption_key)


if __name__ == '__main__':
    main()
