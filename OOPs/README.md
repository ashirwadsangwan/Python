# Object Oriented Programming

Python is an object-oriented programming language. That means it provides features that support object-oriented programming (OOP).

Object-oriented programming has its roots in the 1960s, but it wasn’t until the mid 1980s that it became the main programming paradigm used in the creation of new software. It was developed as a way to handle the rapidly increasing size and complexity of software systems and to make it easier to modify these large and complex systems over time.

Up to now, some of the programs we have been writing use a procedural programming paradigm. In procedural programming the focus is on writing functions or procedures which operate on data. In object-oriented programming the focus is on the creation of objects which contain both data and functionality together. Usually, each object definition corresponds to some object or concept in the real world and the functions that operate on that object correspond to the ways real-world objects interact.

In Python, every value is actually an object. Whether it be a dictionary, a list, or even an integer, they are all objects. Programs manipulate those objects either by performing computation with them or by asking them to perform methods. To be more specific, we say that an object has a **state** and a collection of **methods** that it can perform. (More about methods below.) The state of an object represents those things that the object knows about itself. The state is stored in **instance variables**.

![alt text](https://fopp.umsi.education/runestone/static/fopp/_images/objectpic1.png)

During the initialization of the objects, we created two attributes called x and y for each object, and gave them both the value 0. You will note that when you run the program, nothing happens. It turns out that this is not quite the case. In fact, two Points have been created, each having an x and y coordinate with value 0. However, because we have not asked the program to do anything with the points, we don’t see any other result.

![alt text](https://fopp.umsi.education/runestone/static/fopp/_images/objectpic4.png)


# Adding Other Methods to a Class
The key advantage of using a class like Point rather than something like a simple tuple (7, 6) now becomes apparent. We can add methods to the Point class that are sensible operations for points. Had we chosen to use a tuple to represent the point, we would not have this capability. Creating a class like Point brings an exceptional amount of “organizational power” to our programs, and to our thinking. We can group together the sensible operations, and the kinds of data they apply to, and each instance of the class can have its own state.

A method behaves like a function but it is invoked on a specific instance. For example, with a list bound to variable L, `L.append(7)` calls the function append, with the list itself as the first parameter and 7 as the second parameter. Methods are accessed using dot notation. This is why `L.append(7)` has 2 parameters even though you may think it only has one: the list stored in the variable L is the first parameter value and 7 is the second.

Let’s add two simple methods to allow a point to give us information about its state. The getX method, when invoked, will return the value of the x coordinate.

The implementation of this method is straight forward since we already know how to write functions that return values. One thing to notice is that even though the getX method does not need any other parameter information to do its work, there is still one formal parameter, self. As we stated earlier, all methods defined in a class that operate on objects of that class will have self as their first parameter. Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.


# Objects as Arguments and Parameters

You can pass an object as an argument to a function, in the usual way.

Here is a simple function called distance involving our new Point objects. The job of this function is to figure out the distance between two points.

# Converting an Object to a String
When we’re working with classes and objects, it is often necessary to print an object (that is, to print the state of an object).

The print function shown above produces a string representation of the Point p. The default functionality provided by Python tells you that p is an object of type Point. However, it does not tell you anything about the specific state of the point.

We can improve on this representation if we include a special method call `__str__`. Notice that this method uses the same naming convention as the constructor, that is two underscores before and after the name. It is common that Python uses this naming technique for special methods.

The `__str__` method is responsible for returning a string representation as defined by the class creator. In other words, you as the programmer, get to choose what a Point should look like when it gets printed. In this case, we have decided that the string representation will include the values of x and y as well as some identifying text. It is required that the `__str__` method create and return a string.

Whatever string the `__str__` method for a class returns, that is the string that will print when you put any instance of that class in a print statement. For that reason, the string that a class’s `__str__ `method returns should usually include values of instance variables. If a point has x value 3 and y value 4, but another point has x value 5 and y value 9, those two Point objects should probably look different when you print them, right?


# Instances as Return Values
Functions and methods can return objects. This is actually nothing new since everything in Python is an object and we have been returning values for quite some time. (You can also have lists or tuples of object instances, etc.) The difference here is that we want to have the method create an object using the constructor and then return it as the value of the method.

Suppose you have a point object and wish to find the midpoint halfway between it and some other target point. We would like to write a method, let’s call it **halfway**, which takes another **Point** as a parameter and returns the **Point** that is halfway between the point and the target point it accepts as input.


# Sorting Lists of Instances
Sorting lists of instances of a class is not fundamentally different from sorting lists of objects of any other type. There is a way to define a default sort order for instances, right in the class definition, but it requires defining a bunch of methods or one complicated method, so we won’t bother with that. Instead, you should just provide a key function as a parameter to sorted (or sort).

Previously, you have seen how to provide such a function when sorting lists of other kinds of objects. For example, given a list of strings, you can sort them in ascending order of their lengths by passing a key parameter. Note that if you refer to a function by name, you give the name of the function without parentheses after it, because you want the function object itself. The sorted function will take care of calling the function, passing the current item in the list. Thus, in the example below, we write `key=len` and not `key=len()`.


Sometimes you will find it convenient to define a method for the class that does some computation on the data in an instance. In this case, our class is too simple to really illustrate that. But to simulate it, I’ve defined a method `sort_priority` that just returns the price that’s stored in the instance. Now, that method, `sort_priority` takes one instance as input and returns a number. So it is exactly the kind of function we need to provide as the key parameter for sorted. Here it can get a little confusing: to refer to that method, without actually invoking it, you can refer to `Fruit.sort_priority`. This is analogous to the code above that referred to len rather than invoking `len()`.
