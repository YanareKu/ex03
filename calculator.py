"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *

def main():
    input_num = raw_input("> ")
    math_tokens = input_num.split(" ")
    arith = math_tokens[0]
    num1 = int(math_tokens[1])
    num2 = int(math_tokens[2])
    if arith == "+":
        print add(num1, num2)
    return


if __name__ == '__main__':
    main()
