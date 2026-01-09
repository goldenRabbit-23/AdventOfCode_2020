import sys
import re


def main():
    data = open(sys.argv[1]).read().split('\n')
    memory = {}

    for line in data:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        else:
            addr, val = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
            addr, val = int(addr), int(val)
            val_bin = list(f'{val:036b}')

            for i, bit in enumerate(mask):
                if bit != 'X':
                    val_bin[i] = bit

            memory[addr] = int(''.join(val_bin), 2)

    print(sum(memory.values()))


if __name__ == '__main__':
    main()
