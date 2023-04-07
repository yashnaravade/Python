# inheritance is a way to create a new class for using details of an existing class without modifying it.

class Parent:        # define parent class
    parentAttr = 100
    def __init__(self): # Constructor method for the class Parent. self is a reference to the current instance of the class and is used to access variables that belongs to the class.
        print ("Calling parent constructor")

    def parentMethod(self): # Method of the class Parent
        print ('Calling parent method')

    def setAttr(self, attr): # Method of the class Parent
        Parent.parentAttr = attr

    def getAttr(self): # Method of the class Parent
        print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
    def __init__(self): # Constructor method for the class Child
        print ("Calling child constructor")

    def childMethod(self): # Method of the class Child
        print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.getAttr()          # calls parent's method. 
print("Set attribute value of parent class to 200")
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


