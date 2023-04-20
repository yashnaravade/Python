#method resolution order

class A:
    def __init__(self):
        print("A")
        super().__init__()

class B:
    def __init__(self):
        print("B")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, A):
    def __init__(self):
        print("D")
        super().__init__()

D = D()
# print the method resolution order
print(D.__class__.mro())
# D is an instance of the class D. 
# D.__class__ is the class of D.
# D.__class__.mro() is the method resolution order of the class of D.


# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>) 
# D -> B -> A -> object (object is the base class for all classes in Python) 

# help function in mro

print(help(D.__class__.mro())) # help function in mro 
