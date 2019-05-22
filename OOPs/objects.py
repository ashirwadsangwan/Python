import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

def distance(point1, point2):
    xdiff = point2.getX()-point1.getX()
    ydiff = point2.getY()-point1.getY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4,3)
q = Point(0,0)
print(distance(p,q)) #using an object inside a function.


'''
We could have made distance be a method of the Point class. Then, we would
have called the first parameter self, and would have invoked it using the
dot notation, as in the following code. Which way to implement it is a
matter of coding style. Both work correctly.
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

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distance(self, point2):
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(4,3)
q = Point(0,0)
print(p.distance(q))


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

p = Point(7,6)
print(p)

# Checking Your understanding.
'''
Create a class called Cereal that accepts three inputs: 2 strings and 1
integer, and assigns them to 3 instance variables in the constructor: name,
brand, and fiber. When an instance of Cereal is printed, the user should see
the following: “[name] cereal is produced by [brand] and has [fiber integer]
grams of fiber in every serving!” To the variable name c1, assign an instance
of Cereal whose name is "Corn Flakes", brand is "Kellogg's", and fiber is 2.
To the variable name c2, assign an instance of Cereal whose name is "Honey
Nut Cheerios", brand is "General Mills", and fiber is 3. Practice printing
both!
'''

class Cereal:

    def __init__(self, name, brand, fiber):
        self.name = name
        self.brand = brand
        self.fiber = fiber

    def __str__(self):
        return '{} cereal is produced by {} brand and has {} grams of fiber in every serving!'.format(self.name, self.brand, self.fiber)

c1 = Cereal('Corn Flakes', "Kellogg's", 2)
c2 = Cereal('Honet Nut Cheerios', 'General Mills', 3)

print(c1)
print(c2)

'''
Suppose you have a point object and wish to find the midpoint halfway
between it and some other target point. We would like to write a method,
let’s call it halfway, which takes another Point as a parameter and returns
the Point that is halfway between the point and the target point it accepts
as input.
'''

class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)
# note that you would have exactly the same result if you instead wrote
# mid = q.halfway(p)
# because they are both Point objects, and the middle is the same no matter what

print(mid)
print(mid.getX())
print(mid.getY())


'''
Sometimes you will find it convenient to define a method for the class that
does some computation on the data in an instance. In this case, our class is
too simple to really illustrate that.
'''

class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
print("-----sorted by price, referencing a class method-----")
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

print("---- one more way to do the same thing-----")
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)
