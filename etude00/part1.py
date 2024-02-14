# Project title: Etude 00
# Roland Yang
# 2/1/24
# On my honor, I have neither given nor received unauthorized help on this
# assignment
# Part 1 of the Etude00 asignment.

def print_in(x):
    """ Accept input and print out the input to the terminal with a newline. """
    ret = input(x)
    print(ret)
    return ret

def main():
    # Take input and convert to float to avoid repetition.
    float_in = lambda p: float(print_in(p))
    lbs = float_in("Enter your weight in pounds: ")
    ins = float_in("Enter your height in feet: ")*12
    ins += float_in("Enter your remaining height in inches: ") # 1 foot = 12 in
    print("Your BMI is",round(703*lbs/ins**2,2)) # round to 2 decimal places

if __name__ == "__main__":
    main()