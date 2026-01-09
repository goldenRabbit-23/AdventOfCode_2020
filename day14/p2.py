import sys
import re


def main():
    data = open(sys.argv[1]).read().split('\n')
    memory = {}

    def generate(addr_bin, idx=0):
        if idx == len(addr_bin):
            yield addr_bin
            return

        if addr_bin[idx] == 'X':
            for bit in ('0', '1'):
                addr_bin[idx] = bit
                yield from generate(addr_bin, idx + 1)
            addr_bin[idx] = 'X'
        else:
            yield from generate(addr_bin, idx + 1)

    for line in data:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        else:
            addr, val = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
            addr, val = int(addr), int(val)
            addr_bin = list(f'{addr:036b}')

            for i, bit in enumerate(mask):
                if bit == '1':
                    addr_bin[i] = '1'
                elif bit == 'X':
                    addr_bin[i] = 'X'

            for generated_addr in generate(addr_bin):
                memory[int(''.join(generated_addr), 2)] = val

    print(sum(memory.values()))


if __name__ == '__main__':
    main()
