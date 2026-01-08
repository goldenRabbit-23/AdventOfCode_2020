import sys
from z3 import Optimize, Int, sat


def main():
    buses = open(sys.argv[1]).read().split('\n')[1]
    buses = [(i, int(bus)) for i, bus in enumerate(buses.split(',')) if bus != 'x']

    opt = Optimize()
    t = Int('t')
    opt.add(t >= 0)
    opt.add(((t + i) % bus == 0) for i, bus in buses)
    opt.minimize(t)

    if opt.check() == sat:
        m = opt.model()
        print(m[t].as_long())


if __name__ == '__main__':
    main()
