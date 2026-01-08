import sys


def main():
    earliest, buses = open(sys.argv[1]).read().split('\n')
    earliest = int(earliest)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']
    wait_times = [(bus - (earliest % bus), bus) for bus in buses]
    wait_time, bus_id = min(wait_times)
    print(wait_time * bus_id)


if __name__ == '__main__':
    main()
