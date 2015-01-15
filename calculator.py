"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
from arithmetic import *

def main():
    while True:
        input_num = raw_input("> ")
        math_tokens = input_num.split(" ")
        token_cnt = len(math_tokens)
        if token_cnt == 3:
            arith = math_tokens[0]
            numb1 = int(math_tokens[1])
            numb2 = int(math_tokens[2])
            if arith == "+":
                print add(numb1, numb2)
                continue
            elif arith == "-":
                print subtract(numb1, numb2)
                continue
            elif arith == "*":
                print multiply(numb1, numb2)
                continue
            elif arith == "/":
                print divide(numb1, numb2)
                continue
            elif arith == "pow":
                print power(numb1, numb2)
                continue
            elif arith == "mod":
                print mod(numb1, numb2)
                continue
        if token_cnt == 2:
            arith = math_tokens[0]
            numb1 = int(math_tokens[1])
            if arith == "square":
                print square(numb1)
                continue
            elif arith == "cube":
                print cube(numb1)
                continue
        if math_tokens[0] == "q":
            break
 


if __name__ == '__main__':
    main()
