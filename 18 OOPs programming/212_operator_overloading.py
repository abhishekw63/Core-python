'''
->Operator Overloading is where operators  behave differently in different situations.
->plus is working differently in different situation so here we are achieving pollymorphism
->10+5 (both are integers)
->10+6.8 (int and float)
->'hello'+'world' (both string)
->(1+7j) +(4+6j) (both are complex numbers)
->Python supports operator overloading.
    Binary operators,comparision operators,assignment operators are there.

'''
class Rational():
    def __init__(self,p=1,q=1):
        self.p=p
        self.q=q
    def __add__(self,other): #must write add only
        if isinstance(other, Rational):
            s=Rational()
            s.p=self.p *other.q + other.p * self.q
            s.q=self.q*other.q
            return s
    def __str__(self): #how it is printing ? shouldnt i write s here and s.p and s.q below?
        return f'{self.p}/{self.q}'

r1=Rational(2,3) 
r2=Rational(5,7)

sum=r1+r2
print(sum.p,sum.q)
print(sum)
# try other method such as __mul__,__floor__
