from RationalNumberClass import *

def main():
    """ Testing code. """

    # Try to create a rational number with a zero denominator
    try:
        a = RationalNumber(1, 0)
        assert False
    except AssertionError:
        pass

    a = RationalNumber(1, 2)
    # Test gcd.
    assert a.__gcd__(99, 100) == 1

    b = RationalNumber(1, 2)
    # Test whether the two numbers are alike
    assert a.isLike(b)

    # Try to add two numbers.
    a.add(b)
    assert a == RationalNumber(4, 4)
    # Try to reduce.
    a.__reduce__()
    assert a == RationalNumber(1, 1)

    # Try to subtract two numbers.
    a.subtract(b)
    assert a == RationalNumber(1, 2)

    # Try to multiply two numbers.
    a.multiply(b)
    assert a == RationalNumber(1, 4)

    # Try to divide.
    a.divide(b)
    assert a == RationalNumber(2, 4)
    try:
        b = RationalNumber(0, 1)
        # Try to divide by zero.
        a.divide(b)
        assert False
    except AssertionError:
        pass


if __name__ == '__main__':
    main()