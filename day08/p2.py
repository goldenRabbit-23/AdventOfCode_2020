import sys


def main():
    data = open(sys.argv[1]).read().split('\n')
    instructions = [line.split() for line in data]
    length = len(instructions)

    def simulate(flip_index):
        pointer = 0
        executed = set()
        accumulator = 0

        while pointer < length:
            if pointer in executed:
                return False, -1

            executed.add(pointer)
            operation, argument = instructions[pointer]
            argument = int(argument)

            if pointer == flip_index:
                operation = 'nop' if operation == 'jmp' else 'jmp'

            if operation == 'acc':
                accumulator += argument
                pointer += 1
            elif operation == 'jmp':
                pointer += argument
            elif operation == 'nop':
                pointer += 1

        return True, accumulator

    for i, (op, _) in enumerate(instructions):
        if op in ('jmp', 'nop'):
            ok, accumulator = simulate(i)
            if ok:
                print(accumulator)
                break


if __name__ == '__main__':
    main()
