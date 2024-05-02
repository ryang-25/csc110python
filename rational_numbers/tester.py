# tester.py
# Roland Yang
# 5/1/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

from RationalNumberClass import *

def main():
    """ Testing code. """

    # Try to create a rational number with a zero denominator
    a = RationalNumber(1, 0)
    assert a.getDenominator() == 1

    a = RationalNumber(1, 2)
    # Test gcd.
    assert a.__gcd__(99, 100) == 1

    b = RationalNumber(1, 2)
    # Test whether the two numbers are alike
    assert a.isLike(b)

    # Try to add two numbers.
    a = a.add(b)
    assert a.isLike(RationalNumber(1, 1))

    # Try to subtract two numbers.
    a = a.subtract(b)
    assert a.isLike(RationalNumber(1, 2))

    # Try to multiply two numbers.
    a = a.multiply(b)
    assert a.isLike(RationalNumber(1, 4))

    # Try to divide.
    a = a.divide(b)
    assert a.isLike(RationalNumber(2, 4))

if __name__ == '__main__':
    main()
