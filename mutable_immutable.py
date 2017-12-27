
#Numbers, strings, and tuples are the fundamental types that are immutable.
#Mutable objects include lists, dictionaries and some other objects, depending upon their implementation.


#Integers are immutable objects in Python

#x and y stores the references to the object
x=42
print(id(x))

y=42
print(id(y))        # id of x and y is same since both are referring to same integer 42

x=43                #actual immutable value is not changed. we simply changed the variable to refer to a different object
print(id(x))

#x assigned back to 42
x=42
print(id(x))