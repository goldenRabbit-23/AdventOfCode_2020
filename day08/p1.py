import sys


def main():
    data = open(sys.argv[1]).read().split('\n')
    instructions = [line.split() for line in data]
    pointer = 0
    executed = set()
    accumulator = 0

    while True:
        if pointer in executed:
            print(accumulator)
            break

        executed.add(pointer)
        operation, argument = instructions[pointer]
        argument = int(argument)

        if operation == 'acc':
            accumulator += argument
            pointer += 1
        elif operation == 'jmp':
            pointer += argument
        elif operation == 'nop':
            pointer += 1


if __name__ == '__main__':
    main()
