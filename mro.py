#multiple inheritance-MRO- method resolution order

class A:
    num=10
class B(A):
    pass
class C(A):
    num=1
class D(B,C):
    pass
print(D.num)

#method resolution goes in order
#since the num var is used in two classes the execution starts at D then checks B C and A
#so num=1 is printed bcoz C is checked before A