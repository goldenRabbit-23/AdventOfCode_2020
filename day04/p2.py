import sys


REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def main():
    data = open(sys.argv[1]).read().split('\n\n')
    valid = 0

    for passport in data:
        passport = passport.replace('\n', ' ')
        for field in passport.split():
            key, value = field.split(':')
            if key == 'byr':
                if not 1920 <= int(value) <= 2002:
                    break
            elif key == 'iyr':
                if not 2010 <= int(value) <= 2020:
                    break
            elif key == 'eyr':
                if not 2020 <= int(value) <= 2030:
                    break
            elif key == 'hgt':
                if value.endswith('cm'):
                    if not 150 <= int(value[:-2]) <= 193:
                        break
                elif value.endswith('in'):
                    if not 59 <= int(value[:-2]) <= 76:
                        break
                else:
                    break
            elif key == 'hcl':
                if not value.startswith('#') or len(value) != 7:
                    break
                if not all(value[i] in '0123456789abcdef' for i in range(1, 7)):
                    break
            elif key == 'ecl':
                if not value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    break
            elif key == 'pid':
                if not len(value) == 9 or not value.isdigit():
                    break
        else:
            valid += all(f"{field}:" in passport for field in REQUIRED_FIELDS)

    print(valid)


if __name__ == '__main__':
    main()
