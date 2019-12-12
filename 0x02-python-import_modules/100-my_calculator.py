#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    options = {"+": add, "-": sub, "*": mul, "/": div}
    count = len(argv) - 1
    if (count < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    oper = argv[2]

    if oper not in options:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    total = options[oper](a, b)
    print("{} {} {} = {}".format(a, oper, b, total))
