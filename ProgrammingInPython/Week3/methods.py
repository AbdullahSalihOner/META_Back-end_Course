class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
print(F.mro())

# How can I write factorial method
 #How can I use factorial



# Path: Week3\methods.py
class A:
    def d(self):
        return "Function inside A"
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)
    
   

a = A()
print(a.factorial(5))



