class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

    '''
    Every class should have a method with the special name __init__.
    This initializer method, often referred to as the constructor,
    is automatically called whenever a new instance of Point is created.
    It gives the programmer the opportunity to set up the attributes
    required within the new instance by giving them their initial
    state values. The self parameter (you could choose any other name,
    but nobody ever does!) is automatically set to reference the newly
    created object that needs to be initialized.
    '''

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p) #<__main__.Point object at 0x10e5a52e8>
print(q)  #<__main__.Point object at 0x10e5a5278>

print(p is q)   #False
'''
Both p and q here are objects of the class point but both are different so
it returns as False.
'''

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


m = Point(7,6)
print(m.getX())
print(m.getY())


## Assignment
'''
Create a class called Animal that accepts two numbers as inputs and assigns
them respectively to two instance variables: arms and legs. Create an instance
method called limbs that, when called, returns the total number of limbs the
animal has. To the variable name spider, assign an instance of Animal that has
4 arms and 4 legs. Call the limbs method on the spider instance and save the
result to the variable name spidlimbs.
'''

class Animal:

    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def limbs(self):
        return self.arms + self.legs

spider = Animal(4, 4)
spidlimbs = spider.limbs()
print(spidlimbs)           
