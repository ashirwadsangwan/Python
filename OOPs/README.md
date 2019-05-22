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

A method behaves like a function but it is invoked on a specific instance. For example, with a list bound to variable L, L.append(7) calls the function append, with the list itself as the first parameter and 7 as the second parameter. Methods are accessed using dot notation. This is why L.append(7) has 2 parameters even though you may think it only has one: the list stored in the variable L is the first parameter value and 7 is the second.

Let’s add two simple methods to allow a point to give us information about its state. The getX method, when invoked, will return the value of the x coordinate.

The implementation of this method is straight forward since we already know how to write functions that return values. One thing to notice is that even though the getX method does not need any other parameter information to do its work, there is still one formal parameter, self. As we stated earlier, all methods defined in a class that operate on objects of that class will have self as their first parameter. Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.
