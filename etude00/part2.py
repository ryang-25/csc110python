# Project title: Etude 00
# Roland Yang
# 2/1/24
# On my honor, I have neither given nor received unauthorized help on this
# assignment
# Part 2 of the Etude00 asignment.

from part1 import print_in

def main():
    a = print_in("Enter a value: ")
    b = print_in("Enter a second value: ")
    operators = ["+","-","*","//","/","%"] # calculator operators
    expressions = [f"{a} {op} {b}" for op in operators] # create arithmetic expressions
    for expr in expressions:
        print(expr, "=", eval(expr)) # print expression and evaluate the result

if __name__ == "__main__":
    main()
