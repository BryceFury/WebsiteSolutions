"""

February 2016

Hackerrank - Python - Introduction - Power - Mod Power

So far, we have only heard of Python's powers. Now, we will witness them!

Powers or exponents in Python can be calculated using the built-in power function. Call the power function abab as shown below:

>>> pow(a,b)
or

>>> a**b
It's also possible to calculate abmodmabmodm.

>>> pow(a,b,m)
This is very helpful in computations where you have to print the resultant % mod.

Note: Here, aa and bb can be floats or negatives, but, if a third argument is present, bb cannot be negative.

Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. Frankly speaking, we will never use math.pow().

Task
You are given three integers: aa, bb, and mm, respectively. Print two lines.
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

Input Format
The first line contains aa, the second line contains bb, and the third line contains mm.


"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

STDFIR = int(raw_input())
STDSEC = int(raw_input())
STDM = int(raw_input())

print pow(STDFIR, STDSEC)
print pow(STDFIR, STDSEC, STDM)



