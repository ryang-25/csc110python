def sum(numbers):
    """ Sum a list. """
    acc = 0
    for n in numbers:
        acc += n
    return acc

def main():
    # use a Tamerlane's board
    squares = 10*11 + 2
    rice_squares = [2**n for n in range(0, squares)]
    total_rice = sum(rice_squares)
    # https://www2.census.gov/library/publications/decennial/2010/cph-2/cph-2-1.pdf
    surface_area = 32_020.49


# how long would it take the largest producing country in the world to 