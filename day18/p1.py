import sys


def evaluate(expr):
    val, op = 0, '+'

    while expr:
        token = expr.pop(0)
        if token.isdigit():
            val = val + int(token) if op == '+' else val * int(token)
        elif token in '+*':
            op = token
        elif token == '(':
            sub_val = evaluate(expr)
            val = val + sub_val if op == '+' else val * sub_val
        elif token == ')':
            return val
    return val

def main():
    data = open(sys.argv[1]).read().split('\n')
    print(sum(evaluate(list(line.replace(' ', ''))) for line in data))


if __name__ == '__main__':
    main()
