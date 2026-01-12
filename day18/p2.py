import sys


def evaluate(expr):
    product = 1
    sum_part = 0
    op = '+'

    while expr:
        token = expr.pop(0)
        if token.isdigit():
            value = int(token)
        elif token in '+*':
            op = token
            continue
        elif token == '(':
            value = evaluate(expr)
        elif token == ')':
            return product * sum_part

        if op == '+':
            sum_part += value
        elif op == '*':
            product *= sum_part
            sum_part = value

    return product * sum_part

def main():
    data = open(sys.argv[1]).read().split('\n')
    print(sum(evaluate(list(line.replace(' ', ''))) for line in data))


if __name__ == '__main__':
    main()
