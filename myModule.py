class Calsi:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1+n2

class Math:
    def power(bval,eval):
        return bval**eval
    def isEven(val):
        if val%2==0:
            return True
        return False

def isOdd(val):
    if val%2!=0:
        return True
    return False
class Calsi1:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __add__(self):
        return self.n1+self.n2
    def  __mul__(self):
        return self.n1*self.n2
