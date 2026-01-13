import sys
import re


def main():
    rules_raw, messages = open(sys.argv[1]).read().split('\n\n')
    rules = dict(line.split(': ') for line in rules_raw.split('\n'))

    def regexify(n):
        rule = rules[n]
        if '"' in rule: return rule.strip('"')
        return f"({'|'.join(''.join(regexify(sub) for sub in part.split()) for part in rule.split(' | '))})"

    pattern = re.compile(f"^{regexify('0')}$")
    print(sum(bool(pattern.match(m)) for m in messages.split('\n')))


if __name__ == '__main__':
    main()
