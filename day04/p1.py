import sys


REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def main():
    data = open(sys.argv[1]).read().split('\n\n')
    valid = 0

    for passport in data:
        passport = passport.replace('\n', ' ')
        valid += all(f"{field}:" in passport for field in REQUIRED_FIELDS)

    print(valid)


if __name__ == '__main__':
    main()
