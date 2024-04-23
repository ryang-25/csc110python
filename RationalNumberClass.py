class RationalNumber():
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
        assert denominator != 0

    def __gcd__(self, num1, num2):
        """ Takes the gcd using the euclidian algorithm. The dividend is the
            remainder of the last division operation. """
        while num1 % num2 != 0:
            num1, num2 = num2, num1 % num2
        return num2

    def __eq__(self, n):
        return self.numerator == n.numerator and self.denominator == n.denominator

    def isLike(self, n):
        return self == n

    def __reduce__(self):
        gcd = self.__gcd__(self.numerator, self.denominator)
        self.numerator /= gcd
        self.denominator /= gcd

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, n):
        self.numerator *= n.denominator
        self.numerator += n.numerator * self.denominator
        self.denominator *= n.denominator

    def divide(self, n):
        """ Multiplies by the reciprocal of the number. """
        self.multiply(n.reciprocal())

    def getDenominator(self):
        """ Returns the denominator instance variable """
        return self.denominator

    def getNumerator(self):
        """ Returns the numerator instance variable """
        return self.numerator

    def multiply(self, n):
        """ Multiplies the numerators and the denominators."""
        self.numerator *= n.numerator
        self.denominator *= n.denominator

    def reciprocal(self):
        return RationalNumber(self.denominator, self.numerator)

    def subtract(self, n):
        self.add(RationalNumber(-n.numerator, n.denominator))
