class Rational:
    def __init__(self,p,q):
        self.p=p
        self.q=q
    def __add__(self,other):
        numerator=(self.p * other.q) + (self.q * other.p)
        denominator=self.q *other.q
        sum=Rational(numerator,denominator)
        return sum

    def __str__(self):
        return f'value is {self.p}/{self.q}'

val1=Rational(4,5)
print(val1)
val2=Rational(4,11)

val3=val1+val2

print(f'Sum of {val1} and {val2} is {val3}')

