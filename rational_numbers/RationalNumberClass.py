# RationalNumberClass.py
# Roland Yang
# 5/1/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

class RationalNumber:
    """
    Represents one rational number with a numerator and denominator.
    """

    def __init__(self, numer, denom):
        """Constructor: Sets up the rational number by ensuring a nonzero
denominator and making only the numerator signed. Non-integers are converted."""
        self.numer = int(numer)
        self.denom = int(denom)
        # this is wrong! it will give different results when dividing by zero!
        if denom == 0:
            self.denom = 1
        elif denom < 0:
            self.numer *= -1
            self.denom *= -1
        self.__reduce__()

    def __gcd__(self, num1, num2):
        """Computes and returns the greatest common divisor of the two
positive parameters. Uses Euclid's algorithm."""
        while num1 % num2 != 0:
            num1, num2 = num2, num1 % num2
        return num2

    def isLike(self, op2):
        """Determines if this rational number is equal to the one passed
as a parameter. Assumes they are both reduced.
"""
        return self.numer == op2.numer and self.denom == op2.denom

    def __reduce__(self):
        """Reduces this rational number by dividing both the numerator
and the denominator by their greatest common divisor."""
        gcd = self.__gcd__(self.numer, self.denom)
        self.numer //= gcd
        self.denom //= gcd

    def __str__(self):
        """Returns this rational number as a string."""
        return f"{self.numer}/{self.denom}"

    def add(self, op2):
        """Adds this rational number to the one passed as a parameter.
A common denominator is found by multiplying the individual
denominators."""
        numer = self.numer * op2.denom
        numer += op2.numer * self.denom
        denom = self.denom * op2.denom
        return RationalNumber(numer, denom)

    def divide(self, op2):
        """Divides this rational number by the one passed as a parameter
by multiplying by the reciprocal of the second rational."""
        return self.multiply(op2.reciprocal())

    def getDenominator(self):
        """Returns the denominator of this rational number."""
        return self.denom

    def getNumerator(self):
        """Returns the numerator of this rational number."""
        return self.numer

    def multiply(self, op2):
        """Multiplies this rational number by the one passed as a
parameter."""
        numer = self.numer * op2.numer
        denom = self.denom * op2.denom
        return RationalNumber(numer, denom)

    def reciprocal(self):
        """Returns the reciprocal of this rational number."""
        return RationalNumber(self.denom, self.numer)

    def subtract(self, op2):
        """Subtracts the rational number passed as a parameter from this
rational number."""
        return self.add(RationalNumber(-op2.numer, op2.denom))
