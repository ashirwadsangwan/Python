# ALGORITHMS

## Karatsuba Multiplication
To get a feel for Karatsuba multiplication, let’s re-use our previous
example with `x = 5678` and `y = 1234`. We’re going to execute a
sequence of steps, quite different from the grade-school algorithm,
culminating in the product x · y. The sequence of steps should strike
you as very mysterious, like pulling a rabbit out of a hat; later in
the section we’ll explain exactly what Karatsuba multiplication is
and why it works. The key point to appreciate now is that there’s
a dazzling array of options for solving computational problems like
integer multiplication.
First, to regard the first and second halves of x as numbers in their
own right, we give them the names `a` and `b` (so `a = 56 and b = 78`).
Similarly, `c and d` denote `12 and 34`, respectively.

Next we’ll perform a sequence of operations that involve only the
double-digit numbers a, b, c, and d, and finally collect all the terms
together in a magical way that results in the product of x and y.

```
Step 1: Compute a · c = 56 · 12, which is 672 (as you’re welcome to
check).

Step 2: Compute b · d = 78 · 34 = 2652.
The next two steps are still more inscrutable.

Step 3: Compute (a + b) · (c + d) = 134 · 46 = 6164.

Step 4: Subtract the results of the first two steps from the result of the third step: 6164  672  2652 = 2840.

Step 5: Compute 104 · 672 + 102 · 2840 + 2652 =
6720000 + 284000 + 2652 = 7006652.```
